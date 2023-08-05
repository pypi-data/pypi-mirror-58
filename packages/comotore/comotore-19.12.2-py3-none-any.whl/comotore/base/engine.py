"""
    Component engine class
"""

import asyncio
import warnings
import logging
import traceback
import sys
import multiprocessing
import os
import signal
import functools
import queue
import async_timeout
import textwrap
import uuid

from comotore.base.component import (
    Component,
    ComponentHandler,
    ComponentSignal, ComponentInvokedSignal,
    ComponentRunSignal, ComponentStopSignal, ComponentStopWorldSignal
)
from comotore.errors import ErrorEndOfResponse
from comotore.logging import LOGGER_INTERNAL_NAME, ComotoreLogger, CallbackRecordHandler


class EngineComponents(object):
    def __init__(self):
        self._components = {}

    def __repr__(self):
        representation = "<Components:\n"
        if len(self._components) > 0:
            for component in self._components:
                representation += textwrap.indent("{component}\n".format(component=component), " " * 4)
        else:
            representation += textwrap.indent("---", " " * 4) + "\n"
        representation += ">"
        return representation

    def __contains__(self, component):
        return component in self._components

    def __iter__(self):
        return self._components.__iter__()

    @property
    def is_empty(self):
        return len(self._components) == 0

    def build(self, component):
        self._components[component] = None

    def destroy(self, component):
        if component in self._components:
            del self._components[component]
        else:
            warnings.warn(
                "Try destroy unknown component {component}".format(component=component), RuntimeWarning
            )

    def fix_run(self, component, future):
        if component in self._components:
            self._components[component] = future
        else:
            warnings.warn(
                "Try fix run unknown component {component}".format(component=component), RuntimeWarning
            )

    def fix_stop(self, component):
        if component in self._components:
            self._components[component] = None
        else:
            warnings.warn(
                "Try fix stop unknown component {component}".format(component=component), RuntimeWarning
            )

    def is_running(self, component):
        if component in self._components:
            return self._components[component] is not None
        else:
            warnings.warn(
                "Try check running unknown component {component}".format(component=component), RuntimeWarning
            )

    def try_stop(self, component):
        if component in self._components:
            self._components[component].cancel()
        else:
            warnings.warn(
                "Try stopping unknown component {component}".format(component=component), RuntimeWarning
            )


class EngineConnections(object):
    def __init__(self):
        self._connections = {}

    def __repr__(self):
        representation = "<Connections:\n"
        if len(self._connections) > 0:
            for (sender, method) in self._connections:
                r_points = self._connections[(sender, method)]
                for (receiver, handler) in r_points:
                    need_response = r_points[(receiver, handler)]
                    row = "<Connection " + ("call" if need_response else "cast")
                    row += " sender={sender}, signal={method}, receiver={receiver}, handler={handler}".\
                        format(
                            sender=sender,
                            method="<{name}>".format(name=method.__name__),
                            receiver=receiver,
                            handler="<{name}>".format(name=handler.__name__),
                        )
                    row += ", " + str(self.release_counter(sender, method)) + " releases>" if need_response else ">"
                    representation += textwrap.indent(row, " " * 4) + "\n"
        else:
            representation += textwrap.indent("---", " " * 4) + "\n"
        representation += ">"
        return representation

    def __iter__(self):
        return self._connections.__iter__()

    def build(self, sender, method, receiver, handler, need_response):
        s_point = (sender, method)
        r_point = (receiver, handler)
        if s_point in self._connections:
            r_endpoints = self._connections[s_point]
            if r_point not in r_endpoints:
                self._connections[s_point][r_point] = need_response
        else:
            self._connections[s_point] = {}
            self._connections[s_point][r_point] = need_response

    def destroy(self, sender, method, receiver, handler):
        s_point = (sender, method)
        r_point = (receiver, handler)
        if s_point in self._connections and r_point in self._connections[s_point]:
            del self._connections[s_point][r_point]
            if len(self._connections[s_point]) == 0:
                del self._connections[s_point]

    def destroy_by_component(self, component):
        for (sender, method) in self._connections:
            if sender == component:
                del self._connections[(sender, method)]
            else:
                for (receiver, handler) in self._connections[(sender, method)]:
                    if receiver == component:
                        del self._connections[(sender, method)][(receiver, handler)]
                        if len(self._connections[(sender, method)]) == 0:
                            del self._connections[(sender, method)]

    def has_send_endpoint(self, sender, method):
        return (sender, method) in self._connections

    def has_connection(self, sender, method, receiver, handler):
        s_point = (sender, method)
        r_point = (receiver, handler)
        if s_point not in self._connections:
            return False
        if r_point not in self._connections[s_point]:
            return False
        return True

    def release_counter(self, sender, method):
        s_point = (sender, method)
        if s_point in self._connections:
            counter = 0
            for r_point in self._connections[s_point]:
                if self._connections[s_point][r_point]:
                    counter += 1
            return counter
        else:
            return 0

    def receive_points(self, sender, method):
        s_point = (sender, method)
        if s_point in self._connections:
            return [(*r_point, self._connections[s_point][r_point]) for r_point in self._connections[s_point]]
        else:
            return []


class EnginePublications(object):
    def __init__(self):
        self._by_signal = {}
        self._by_name = {}

    def __repr__(self):
        representation = "<Publication:\n"
        if len(self._by_signal) > 0:
            for (sender, method) in self._by_signal:
                row = "<Public sender={sender}, signal={method}, name={name}>".format(
                    sender=sender,
                    method="<{name}>".format(name=method.__name__),
                    name=self._by_signal[(sender, method)]
                )
                representation += textwrap.indent(row, " " * 4) + "\n"
        else:
            representation += textwrap.indent("---", " " * 4) + "\n"
        representation += ">"
        return representation

    def iter_by_signal(self):
        return self._by_signal.__iter__()

    def iter_by_name(self):
        return self._by_name.__iter__()

    def build(self, sender, method, name):
        if (sender, method) not in self._by_signal and name not in self._by_name:
            self._by_signal[(sender, method)] = name
            self._by_name[name] = (sender, method)

    def destroy(self, sender, method, name):
        if (sender, method) in self._by_signal and name in self._by_name:
            del self._by_signal[(sender, method)]
            del self._by_name[name]

    def destroy_by_component(self, component):
        for (sender, method) in self._by_signal:
            if sender == component:
                name = self._by_signal[(sender, method)]
                del self._by_signal[(sender, method)]
                del self._by_name[name]

    def destroy_by_signal(self, sender, method):
        if (sender, method) in self._by_signal:
            name = self._by_signal[(sender, method)]
            if name in self._by_name[name]:
                del self._by_signal[(sender, method)]
                del self._by_name[name]

    def destroy_by_name(self, name):
        if name in self._by_name:
            (sender, method) = self._by_name[name]
            if (sender, method) in self._by_signal[name]:
                del self._by_signal[(sender, method)]
                del self._by_name[name]

    def name_by_signal(self, sender, method):
        if (sender, method) in self._by_signal:
            return self._by_signal[(sender, method)]
        return None

    def signal_by_name(self, name):
        if name in self._by_name:
            return self._by_name[name]
        return None


class EngineAvatar(Component):
    async def quit(self, _):
        await self._out_queue.put(ComponentStopWorldSignal())


class Engine(object):
    def __init__(
            self,
            *,
            loop=None,
            stop_if_empty=False,
            process_count=None,
            is_master=True,
            suppress_runtime_warnings=True
    ):
        self._loop = loop or asyncio.get_event_loop()

        previous_logger_class = logging.getLoggerClass()
        logging.setLoggerClass(ComotoreLogger)
        self._logger = logging.getLogger(LOGGER_INTERNAL_NAME)
        logging.setLoggerClass(previous_logger_class)

        self._components = EngineComponents()
        self._connections = EngineConnections()
        self._publications = EnginePublications()
        self._processing_queue = asyncio.Queue(loop=self._loop)

        self._avatar = None

        self._stop_if_empty = stop_if_empty

        self._is_master = is_master
        self._is_master_entered = False
        self._process_count = max(1, process_count or os.cpu_count() or 2)
        self._process_reservation = {}
        self._processes = {}

        self._suppress_runtime_warnings = suppress_runtime_warnings

        self._in_stopping = asyncio.Event(loop=self._loop)
        self._stopped = asyncio.Event(loop=self._loop)

    def __repr__(self):
        representation = "<Engine at={at}\n".format(at=hex(id(self)))
        representation += textwrap.indent("{list}".format(list=self._components), " " * 4)
        representation += "\n"
        representation += textwrap.indent("{list}".format(list=self._connections), " " * 4)
        representation += "\n"
        representation += textwrap.indent("{list}".format(list=self._publications), " " * 4)
        representation += "\n"
        representation += ">"
        return representation

    def __await__(self):
        return self.run().__await__()

    async def __aenter__(self):
        if self._is_master:
            self._is_master_entered = True
            return self
        else:
            raise RuntimeError("Can't entered in master mode")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self._is_master_entered:
            raise RuntimeError("Must entered in master mode first")
        await self._wait_all()

    @property
    def loop(self):
        return self._loop

    @property
    def logger(self):
        return self._logger

    @property
    def processing_queue(self):
        return self._processing_queue

    @property
    def avatar(self):
        if self._avatar is None:
            self._avatar = self.component(EngineAvatar)
        return self._avatar

    @property
    def stop_if_empty(self):
        return self._stop_if_empty

    @stop_if_empty.setter
    def stop_if_empty(self, value):
        self._stop_if_empty = value

    @property
    def in_stopping(self):
        return self._in_stopping

    @property
    def stopped(self):
        return self._stopped

    @property
    def components(self):
        return self._components

    @property
    def connections(self):
        return self._connections

    @property
    def publications(self):
        return self._publications

    def component(self, component_class, **kwargs):
        if not issubclass(component_class, Component):
            warnings.warn("Proposed class is not Component subclass: {class_}".format(
                class_=component_class.__name__
            ), RuntimeWarning)
            return

        component = component_class(loop=self._loop, engine=self, **kwargs)
        self._components.build(component)
        self._processing_queue.put_nowait(ComponentRunSignal(component))
        return component

    def delete_later(self, component):
        if component not in self._components:
            warnings.warn(
                "Try to delete unknown component {component}".format(component=component), RuntimeWarning
            )
            return
        self._processing_queue.put_nowait(ComponentStopSignal(component))

    async def _delete_component(self, component):
        await component.stopped.wait()
        self._components.fix_stop(component)
        self._connections.destroy_by_component(component)
        self._publications.destroy_by_component(component)
        self._components.destroy(component)

        if self._components.is_empty and self._stop_if_empty:
            self._processing_queue.put_nowait(ComponentStopWorldSignal())

    def has_connection(self, signal_, handler_):
        return self._connections.has_connection(signal_.__self__, signal_.func, handler_.__self__, handler_)

    def _are_signal_conditions_met(self, signal_):
        if not isinstance(signal_.__self__, (Component,)):
            warnings.warn("Signal sender not Component instance: {sender}".format(
                sender=signal_.__self__.__class__
            ), RuntimeWarning)
            return False
        if signal_.__self__ not in self._components:
            warnings.warn("Signal sender is unknown component: {sender}".format(
                sender=signal_.__self__.__class__
            ), RuntimeWarning)
            return False
        return True

    def _are_handler_conditions_met(self, handler_):
        if not isinstance(handler_.__self__, (Component,)):
            warnings.warn("Handler receiver not Component instance: {receiver}".format(
                receiver=handler_.__self__.__class__
            ), RuntimeWarning)
            return False
        if handler_.__self__ not in self._components:
            warnings.warn("Handler receiver is unknown component: {receiver}".format(
                receiver=handler_.__self__.__class__
            ), RuntimeWarning)
            return False
        return True

    def cast(self, signal_, handler_):
        if not self._are_signal_conditions_met(signal_):
            return
        if not self._are_handler_conditions_met(handler_):
            return
        if self.has_connection(signal_, handler_):
            warnings.warn(
                "Connection already exists: {sender}:<{method}> -> {receiver}:<{handler}>".format(
                    sender=signal_.__self__.__class__, method=signal_.func.__name__,
                    receiver=handler_.__self__.__class__, handler=handler_.__name__
                ),
                RuntimeWarning
            )
            return
        self._connections.build(signal_.__self__, signal_.func, handler_.__self__, handler_, False)

    def call(self, signal_, handler_):
        if not self._are_signal_conditions_met(signal_):
            return
        if not self._are_handler_conditions_met(handler_):
            return
        if self.has_connection(signal_, handler_):
            warnings.warn(
                "Connection already exists: {sender}:<{method}> -> {receiver}:<{handler}>".format(
                    sender=signal_.__self__.__class__, method=signal_.func.__name__,
                    receiver=handler_.__self__.__class__, handler=handler_.__name__
                ),
                RuntimeWarning
            )
            return
        self._connections.build(signal_.__self__, signal_.func, handler_.__self__, handler_, True)

    def disconnect(self, signal_, handler_):
        if not self._are_signal_conditions_met(signal_):
            return
        if not self._are_handler_conditions_met(handler_):
            return
        if not self.has_connection(signal_, handler_):
            warnings.warn(
                "Unknown connection: {sender}:<{method}> -> {receiver}:<{handler}>".format(
                    sender=signal_.__self__.__class__, method=signal_.func.__name__,
                    receiver=handler_.__self__.__class__, handler=handler_.__name__
                ),
                RuntimeWarning
            )
            return
        self._connections.destroy(signal_.__self__, signal_.func, handler_.__self__, handler_)

    def publish(self, signal_, name):
        if not self._are_signal_conditions_met(signal_):
            return
        if not isinstance(name, str):
            warnings.warn("Name is not string instance: {name}".format(
                name=name
            ), RuntimeWarning)
            return
        self._publications.build(signal_.__self__, signal_.func, name)

    def hide(self, signal_, name):
        if not self._are_signal_conditions_met(signal_):
            return
        if not isinstance(name, str):
            warnings.warn("Name is not string instance: {name}".format(
                name=name
            ), RuntimeWarning)
            return
        self._publications.destroy(signal_.__self__, signal_.func, name)

    async def _not_found_handler(self, signal_):
        if not self._suppress_runtime_warnings:
            self.logger["Engine"].warning(
                "Not found any handler for sender {sender} signal {method}".format(
                    sender=signal_.sender, method=signal_.method
                )
            )
        await signal_.response_queue.put(ErrorEndOfResponse())

    def _on_exception_component_run(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Engine"].error(
                "Catch exception", stage="Component running",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )

    def _on_exception_component_deleting(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Engine"].error(
                "Catch exception", stage="Component deleting",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )

    async def invoke_cast(self, handler_, payload=None, correlation_id=None):
        _correlation_id = correlation_id or uuid.uuid4()
        signal_ = ComponentInvokedSignal(
            handler_, None, None, payload, need_response=False, correlation_id=_correlation_id, loop=self._loop
        )
        await self._processing_queue.put(signal_)
        return signal_

    async def invoke_call(self, handler_, payload=None, correlation_id=None):
        _correlation_id = correlation_id or uuid.uuid4()
        signal_ = ComponentInvokedSignal(
            handler_, None, None, payload, need_response=True, correlation_id=_correlation_id, loop=self._loop
        )
        await self._processing_queue.put(signal_)
        return signal_

    async def run(self):
        try:
            while True:
                signal_ = await self._processing_queue.get()
                if isinstance(signal_, (ComponentRunSignal,)):
                    if signal_.component in self._components and not self._components.is_running(signal_.component):
                        future = asyncio.ensure_future(signal_.component.run_cycle(), loop=self._loop)
                        future.add_done_callback(self._on_exception_component_run)
                        self._components.fix_run(signal_.component, future)
                elif isinstance(signal_, (ComponentStopSignal,)):
                    if signal_.component in self._components and self._components.is_running(signal_.component):
                        future = asyncio.ensure_future(self._delete_component(signal_.component), loop=self._loop)
                        future.add_done_callback(self._on_exception_component_deleting)
                        await signal_.component.in_queue.put(signal_)
                elif isinstance(signal_, (ComponentStopWorldSignal,)):
                    break
                elif isinstance(signal_, ComponentInvokedSignal):
                    receiver, handler_ = signal_.handler.__self__, signal_.handler
                    if receiver not in self._components:
                        asyncio.ensure_future(self._not_found_handler(signal_), loop=self._loop)
                    signal_.releases_counter = 1
                    await receiver.in_queue.put(
                        ComponentHandler(handler_, signal_, need_response=signal_.need_response)
                    )
                elif isinstance(signal_, (ComponentSignal,)):
                    if self._connections.has_send_endpoint(signal_.sender, signal_.method):
                        receive_points = self._connections.receive_points(signal_.sender, signal_.method)
                        for (receiver, handler, need_response) in receive_points:
                            if signal_.direct_to is None:
                                signal_.releases_counter = self._connections.release_counter(
                                    signal_.sender, signal_.method
                                )
                                await receiver.in_queue.put(
                                    ComponentHandler(handler, signal_, need_response=need_response)
                                )
                            elif receiver in signal_.direct_to:
                                signal_.releases_counter = len(signal_.direct_to)
                                await receiver.in_queue.put(
                                    ComponentHandler(handler, signal_, need_response=need_response)
                                )
                    else:
                        asyncio.ensure_future(self._not_found_handler(signal_), loop=self._loop)
        except asyncio.CancelledError:
            pass
        finally:
            self._in_stopping.set()
            for component in self._components:
                self._components.try_stop(component)
            await asyncio.gather(
                *[component.stopped.wait() for component in self._components], loop=self._loop, return_exceptions=True
            )
            self._stopped.set()

    def fly(self, name, initializer, post_initializer=None):
        self.logger["Engine"].info("Preparing fly subprocess", name=name)
        if not self._is_master_entered:
            raise RuntimeError("Must entered in master mode first")

        if len(self._process_reservation) < self._process_count:
            fake_engine = Engine()
            initializer(fake_engine)
            proxy_signals = [name for name in fake_engine._publications.iter_by_name()]
            has_proxy_signals = len(proxy_signals) > 0

            self._process_reservation[name] = dict(
                initializer=initializer,
                post_initializer=post_initializer,
                has_proxy_signals=has_proxy_signals,
                proxy_signals=proxy_signals
            )
        else:
            self.logger["Engine"].warning(
                "Reached the limit (limit={limit}) of the number of processes. Process will not be created".format(
                    limit=self._process_count
                )
            )

    async def subprocess_log(self, log_queue):
        try:
            while True:
                try:
                    record = log_queue.get_nowait()
                    self.logger.handle(record)
                except queue.Empty:
                    pass

                await asyncio.sleep(0.005)
        except asyncio.CancelledError:
            pass

    async def _wait_all(self):
        log_queue = multiprocessing.Queue()

        try:
            asyncio.ensure_future(self.subprocess_log(log_queue), loop=self._loop)
            for name in self._process_reservation:
                reservation = self._process_reservation[name]
                process = EngineHostProcess(
                    initializer=reservation["initializer"],
                    post_initializer=reservation["post_initializer"],
                    log_queue=log_queue
                )
                self._processes[name] = process
                process.start()
                self.logger["Engine"].info("Subprocess started", pid=process.pid)

            joins = []
            if len(self._processes) > 0:
                joins = [self._processes[name].join() for name in self._processes]
            joins.append(self.run())
            await asyncio.gather(*joins, loop=self._loop, return_exceptions=True)
        except asyncio.CancelledError:
            if len(self._processes) > 0:
                joins = [self._processes[name].join() for name in self._processes]
                await asyncio.gather(*joins, loop=self._loop, return_exceptions=True)
                async with async_timeout.timeout(1, loop=self._loop):
                    await self.subprocess_log(log_queue)
                for name in self._processes:
                    process = self._processes[name]
                    self.logger["Engine"].info(
                        "Subprocess exited", pid=process.pid, exitcode=process.exitcode
                    )


class EngineHostProcess(object):
    def __init__(self, initializer=None, name=None, post_initializer=None, log_queue=None):
        if initializer is None or initializer is not None and asyncio.iscoroutinefunction(initializer):
            raise ValueError("EngineHostProcess initializer must be synchronous function")

        self._initializer = initializer
        self._post_initializer = post_initializer
        self._name = name

        self._process = None
        self._pid = None
        self._exitcode = None
        self._log_queue = log_queue

    @property
    def origin(self):
        return self._process

    @property
    def pid(self):
        return self._pid

    @property
    def exitcode(self):
        return self._exitcode

    @staticmethod
    def run(initializer, post_initializer=None, log_queue=None):
        def logger_callback(record):
            if log_queue is not None:
                log_queue.put_nowait(record)

        logging.setLoggerClass(ComotoreLogger)
        logger = logging.getLogger(LOGGER_INTERNAL_NAME)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        logger.addHandler(CallbackRecordHandler(logger_callback))

        async def runtime_cycle(loop):
            engine = Engine(loop=loop, is_master=False)

            initializer(engine)
            if post_initializer is not None:
                post_initializer(engine)

            await engine

        async def shutdown(loop):
            component_sub_tasks = []
            component_tasks = []
            general_tasks = []

            for task in asyncio.Task.all_tasks(loop=loop):
                if task is not asyncio.tasks.Task.current_task(loop=loop):
                    if hasattr(task, "is_component"):
                        component_tasks.append(task)
                    elif hasattr(task, "is_component_sub"):
                        component_sub_tasks.append(task)
                    else:
                        general_tasks.append(task)

            if len(component_sub_tasks) > 0:
                list(map(lambda _task: _task.cancel(), component_sub_tasks))
                await asyncio.gather(*component_sub_tasks, loop=loop, return_exceptions=True)

            if len(component_tasks) > 0:
                list(map(lambda _task: _task.cancel(), component_tasks))
                await asyncio.gather(*component_tasks, loop=loop, return_exceptions=True)

            if len(general_tasks) > 0:
                list(map(lambda _task: _task.cancel(), general_tasks))
                await asyncio.gather(*general_tasks, loop=loop, return_exceptions=True)

            loop.stop()

        loop_ = asyncio.new_event_loop()
        asyncio.set_event_loop(loop_)

        runtime_cycle_future = asyncio.ensure_future(runtime_cycle(loop_), loop=loop_)

        def signal_interrupt():
            runtime_cycle_future.cancel()

        try:
            for sig in [signal.SIGINT, signal.SIGTERM]:
                loop_.add_signal_handler(sig, functools.partial(signal_interrupt))
        except NotImplementedError:
            async def periodic_nt():
                try:
                    while True:
                        await asyncio.sleep(1)
                except asyncio.CancelledError:
                    pass

            asyncio.ensure_future(periodic_nt(), loop=loop_)

        result = None
        try:
            result = loop_.run_until_complete(runtime_cycle_future)
        except KeyboardInterrupt:
            logger.info("Interrupted", tag="Subprocess")
        finally:
            loop_.run_until_complete(shutdown(loop_))
            if hasattr(loop_, "shutdown_asyncgens"):
                loop_.run_until_complete(loop_.shutdown_asyncgens())
            loop_.close()

        return result

    def start(self):
        self._process = multiprocessing.Process(
            target=EngineHostProcess.run, name=self._name,
            args=(self._initializer,), kwargs=dict(
                post_initializer=self._post_initializer,
                log_queue=self._log_queue
            )
        )
        if not self._process.is_alive() and self._process.exitcode is None:
            self._process.start()
            self._pid = self._process.pid

    async def join(self, on_exit_callback=None):
        if self._process is not None:
            if not self._process.is_alive() and self._process.exitcode is None:
                raise ValueError("Must start process before joining")

            while self._process.exitcode is None:
                await asyncio.sleep(0.005)

            if on_exit_callback is not None:
                on_exit_callback(self._pid, self._process.exitcode)
            self._exitcode = self._process.exitcode
