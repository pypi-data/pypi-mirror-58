"""
    External component - agent of external engine
"""

import asyncio

from comotore.base.component import (Component, ComponentSignal)


class ExternalSignal(object):
    def __init__(self):
        self._key = None
        self._correlation_id = None
        self._headers = {}

        self._payload = None

    @property
    def key(self):
        return self._key

    @property
    def correlation_id(self):
        return self._correlation_id

    @property
    def headers(self):
        return self._headers

    @property
    def payload(self):
        return self._payload


class External(Component):
    _mapping_signal_method_by_key = {}
    _mapping_handler_method_by_key = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._external_income_queue = asyncio.Queue(loop=self._loop)

    def __repr__(self):
        return "<External class={class_}, at={at}>".format(
            class_=self.__class__.__name__,
            at=hex(id(self))
        )

    @classmethod
    def signal(cls, signal_key):
        def real_signal(decorated):
            cls._mapping_signal_method_by_key[signal_key] = decorated

            async def decorator(self):
                raise RuntimeError("Can't send external signal")
            decorator.func = decorated
            return decorator
        return real_signal

    @classmethod
    def handler(cls, handler_key):
        def real_handler(decorated):
            cls._mapping_handler_method_by_key[handler_key] = decorated
            return decorated
        return real_handler

    async def _construct(self):
        self.fly(self._external_run_cycle())
        await super()._construct()

    async def _external_run_cycle(self):
        try:
            while True:
                ex_signal = await self._external_income_queue.get()
                if isinstance(ex_signal, (ExternalSignal,)):
                    method = self._mapping_signal_method_by_key.get(ex_signal.key, None)
                    if method is not None:
                        signal = ComponentSignal(
                            self, method, ex_signal.payload, correlation_id=ex_signal.correlation_id, loop=self._loop
                        )
                        await self.send_signal(signal)
                        # TODO: handle signal response, need determined by ExternalSignal flag 'responsive'
                    else:
                        self.logger["External"].warning(
                            "Not found any signal for key {key}".format(key=ex_signal.key)
                        )
        except asyncio.CancelledError:
            pass
