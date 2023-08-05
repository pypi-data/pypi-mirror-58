"""
    Base component class
"""

import asyncio
import uuid
import logging
import traceback
import sys
import async_timeout
import warnings
import pickle
import textwrap

from comotore.logging import (LOGGER_INTERNAL_NAME, ComotoreLogger)
from comotore.errors import (ErrorEndOfResponse, ErrorTimeoutResponse)


class ComponentStopWorldSignal(object):
    pass


class ComponentRunSignal(object):
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component


class ComponentStopSignal(object):
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component


class ComponentSignal(object):
    def __init__(self, sender, method, payload, correlation_id=None, loop=None, direct_to=None):
        self._sender = sender
        self._method = method

        try:
            pickled = pickle.dumps(payload, protocol=pickle.HIGHEST_PROTOCOL)
        except pickle.PicklingError:
            raise RuntimeError("Can't encode signal {name} payload".format(name=self._method.__name__))
        self._payload = pickled

        self._correlation_id = correlation_id
        self._loop = loop or asyncio.get_event_loop()
        self._response_queue = asyncio.Queue(loop=self._loop)
        self._releases_counter = 0
        self._timeout_caught = False
        self._direct_to = direct_to

        # TODO: add headers concept

    def __repr__(self):
        return (
            "<ComponentSignal at={at}, " +
            "sender={sender}, " +
            "method={method}, " +
            "payload={payload}, " +
            "correlation_id={id}, " +
            "releases_counter={counter}, " +
            "direct_to={direct_to}"
            ">"
        ).format(
            at=hex(id(self)),
            sender=self._sender,
            method=self._method,
            payload=self._payload,
            id=self._correlation_id,
            counter=self._releases_counter,
            direct_to=self._direct_to
        )

    @property
    def sender(self):
        return self._sender

    @property
    def method(self):
        return self._method

    @property
    def payload(self):
        try:
            unpickled = pickle.loads(self._payload)
        except pickle.UnpicklingError:
            raise RuntimeError("Can't decode signal {name} payload".format(name=self._method.__name__))
        return unpickled

    @property
    def correlation_id(self):
        return self._correlation_id

    @property
    def response_queue(self):
        return self._response_queue

    @property
    def releases_counter(self):
        return self._releases_counter

    @releases_counter.setter
    def releases_counter(self, counter):
        self._releases_counter = counter

    @property
    def timeout_caught(self):
        return self._timeout_caught

    @property
    def direct_to(self):
        return self._direct_to

    async def response(self, timeout=None):
        try:
            counter = None
            while True:
                try:
                    async with async_timeout.timeout(timeout, loop=self._loop):
                        res = await self._response_queue.get()
                except asyncio.TimeoutError:
                    res = ErrorTimeoutResponse()
                    self._timeout_caught = True
                if counter is None:
                    counter = self._releases_counter
                if not (isinstance(res, (ErrorEndOfResponse,)) or isinstance(res, (ErrorTimeoutResponse,))):
                    yield res
                else:
                    counter = counter - 1
                    if counter < 1:
                        break
        except asyncio.CancelledError:
            pass


class ComponentInvokedSignal(ComponentSignal):
    def __init__(
            self, handler, sender, method, payload, correlation_id=None, loop=None, need_response=False
    ):
        super().__init__(sender, method, payload, correlation_id=correlation_id, loop=loop)

        self._handler = handler
        self._need_response = need_response

    @property
    def handler(self):
        return self._handler

    @property
    def need_response(self):
        return self._need_response


class ComponentHandler(object):
    def __init__(self, method, signal, need_response=False):
        self._method = method
        self._signal = signal
        self._need_response = need_response

    @property
    def method(self):
        return self._method

    @property
    def signal(self):
        return self._signal

    @property
    def need_response(self):
        return self._need_response

    def __repr__(self):
        return (
            "<ComponentHandler at={at}, " +
            "method={method}, " +
            "signal={signal}, " +
            "need_response={need}" +
            ">"
        ).format(
            at=hex(id(self)),
            method=self._method,
            signal=self._signal,
            need=self._need_response
        )


class Component(object):
    def __init__(self, *, engine=None, start_waiting_for=None, stop_waiting_for=None, **kwargs):
        previous_logger_class = logging.getLoggerClass()
        logging.setLoggerClass(ComotoreLogger)
        self._logger = logging.getLogger(LOGGER_INTERNAL_NAME)
        logging.setLoggerClass(previous_logger_class)

        self._engine = engine
        if self._engine is None:
            raise RuntimeError("Component engine must not be None")
        self._loop = engine.loop
        self._out_queue = self._engine.processing_queue

        self._started = asyncio.Event(loop=self._loop)
        self._stopped = asyncio.Event(loop=self._loop)

        self._start_waiting_for = start_waiting_for
        self._stop_waiting_for = stop_waiting_for

        self._in_queue = asyncio.Queue(loop=self._loop)

        self._fliers = {}
        self._handlers = {}

    def __repr__(self):
        return "<Component class={class_}, at={at}>".format(
            class_=self.__class__.__name__,
            at=hex(id(self))
        )

    def full_repr(self):
        representation = "<Component class={class_}, at={at}\n".format(
            class_=self.__class__.__name__,
            at=hex(id(self))
        )

        representation += textwrap.indent("waiting for on start\n", " " * 4)
        if self._start_waiting_for is None:
            representation += textwrap.indent("---\n", " " * 8)
        else:
            for component in self._start_waiting_for or []:
                representation += textwrap.indent("{component}\n".format(component=component), " " * 8)

        representation += textwrap.indent("waiting for on stop\n", " " * 4)
        if self._stop_waiting_for is None:
            representation += textwrap.indent("---\n", " " * 8)
        else:
            for component in self._stop_waiting_for or []:
                representation += textwrap.indent("{component}\n".format(component=component), " " * 8)

        representation += textwrap.indent("signals\n", " " * 4)
        attrs = [attr for attr in dir(self) if not attr.startswith("__") and hasattr(getattr(self, attr), "func")]
        if len(attrs):
            for attr in attrs:
                representation += textwrap.indent("{attr}\n".format(attr=attr), " " * 8)
        else:
            representation += textwrap.indent("---\n", " " * 8)

        representation += ">"
        return representation

    @classmethod
    def signal(cls, decorated):
        async def decorator(self, payload=None, correlation_id=None, direct_to=None):
            _correlation_id = correlation_id or uuid.uuid4()
            _direct_to = []
            if isinstance(direct_to, (list,)):
                for d in direct_to:
                    if not isinstance(d, (Component,)):
                        warnings.warn("direct class is not Component subclass: {class_}".format(
                            class_=d.__class__.__name__
                        ), RuntimeWarning)
                    else:
                        _direct_to.append(d)
            elif direct_to is None:
                _direct_to = None
            else:
                if not isinstance(direct_to, (Component,)):
                    warnings.warn("direct class is not Component subclass: {class_}".format(
                        class_=direct_to.__class__.__name__
                    ), RuntimeWarning)
                else:
                    _direct_to.append(direct_to)
            signal = ComponentSignal(
                self, decorated, payload, correlation_id=_correlation_id, loop=self._loop, direct_to=_direct_to
            )
            await self.send_signal(signal)
            return signal

        decorator.func = decorated
        return decorator

    @property
    def logger(self):
        return self._logger

    @property
    def loop(self):
        return self._loop

    @property
    def engine(self):
        return self._engine

    @property
    def started(self):
        return self._started

    @property
    def stopped(self):
        return self._stopped

    @property
    def in_queue(self):
        return self._in_queue

    @property
    def start_waiting_for(self):
        return self._start_waiting_for

    @start_waiting_for.setter
    def start_waiting_for(self, value):
        self._start_waiting_for = value

    @property
    def stop_waiting_for(self):
        return self._stop_waiting_for

    @stop_waiting_for.setter
    def stop_waiting_for(self, value):
        self._stop_waiting_for = value

    def component(self, component_class, **kwargs):
        return self._engine.component(component_class, **kwargs)

    def delete_later(self, component):
        self._engine.delete_later(component)

    def cast(self, signal, handler):
        self._engine.cast(signal, handler)

    def call(self, signal, handler):
        self._engine.call(signal, handler)

    def disconnect(self, signal, handler):
        self._engine.disconnect(signal, handler)

    async def send_signal(self, signal):
        if not isinstance(signal, (ComponentSignal,)):
            raise Exception("signal not instance of ComponentSignal")
        await self._out_queue.put(signal)

    async def _construct(self):
        await self.construct()

    async def construct(self):
        pass

    async def _destruct(self):
        await self.destruct()

    async def destruct(self):
        pass

    def fly(self, coro):
        future = asyncio.ensure_future(coro)
        future.add_done_callback(self._on_exception_fly_run)
        self._fliers[future] = True

        return future

    def _on_exception_handler_run(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Component"].error(
                "Catch exception", stage="Handle processing",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )
        finally:
            del self._handlers[future]

    def _on_exception_fly_run(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Component"].error(
                "Catch exception", stage="Fly running",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )
        finally:
            del self._fliers[future]

    @staticmethod
    async def process_handler(handler_):
        coro = handler_.method(handler_.signal)
        if handler_.need_response:
            if hasattr(coro, "__aiter__"):
                async for res in coro:
                    await handler_.signal.response_queue.put(res)
                await handler_.signal.response_queue.put(ErrorEndOfResponse())
            else:
                res = await coro
                await handler_.signal.response_queue.put(res)
                await handler_.signal.response_queue.put(ErrorEndOfResponse())
        else:
            if hasattr(coro, "__aiter__"):
                async for _ in coro:
                    pass
            else:
                await coro

    async def run_cycle(self):
        is_stopping_by_signal = False
        try:
            if self._start_waiting_for is not None:
                await asyncio.gather(*[event.wait() for event in self._start_waiting_for])

            await self._construct()

            self._started.set()

            while True:
                handler = await self._in_queue.get()
                if isinstance(handler, (ComponentStopSignal,)):
                    is_stopping_by_signal = True
                    break
                elif not isinstance(handler, (ComponentHandler,)):
                    continue

                future = asyncio.ensure_future(self.process_handler(handler))
                future.add_done_callback(self._on_exception_handler_run)
                self._handlers[future] = True
        except asyncio.CancelledError:
            pass
        finally:
            if not is_stopping_by_signal:
                await self._engine.in_stopping.wait()
            if self._stop_waiting_for is not None:
                await asyncio.gather(*[event.wait() for event in self._stop_waiting_for], self._loop)
            await asyncio.gather(*[handler for handler in self._handlers if not handler.done()], return_exceptions=True)
            await asyncio.gather(*[flier for flier in self._fliers if not flier.done()], return_exceptions=True)
            await self._destruct()
            self._stopped.set()
