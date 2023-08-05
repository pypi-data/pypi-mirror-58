"""
    Assembly of engines
"""

import asyncio
import logging
import warnings
import sys
import traceback
import re

from comotore.logging import LOGGER_INTERNAL_NAME
from comotore.logging.loggers import ComotoreLogger
from comotore.base.engine import Engine
from comotore.locations import Location


class Assembly(object):
    def __init__(
            self,
            location_key,
            *,
            loop=None
    ):
        self._loop = loop or asyncio.get_event_loop()

        previous_logger_class = logging.getLoggerClass()
        logging.setLoggerClass(ComotoreLogger)
        self._logger = logging.getLogger(LOGGER_INTERNAL_NAME)
        logging.setLoggerClass(previous_logger_class)

        self._location_key_regexp = re.compile("^[0-9a-zA-Z_]+$")
        if not self._location_key_regexp.match(location_key):
            raise RuntimeError("incorrect location key - should satisfy [0-9a-zA-Z_]+")
        self._location_key = location_key
        self._engine = Engine(loop=self._loop)  # TODO: define other engine parameters
        self._processing_queue = asyncio.Queue(loop=self._loop)

        self._locations = []
        self._location_key_location_mapping = {}

        self._engine_future = None
        self._processing_future = None
        self._location_futures = []

    def __await__(self):
        return self.run().__await__()

    @property
    def logger(self):
        return self._logger

    @property
    def engine(self):
        return self._engine

    def location(self, location_key, location_class, *args, **kwargs):
        if not self._location_key_regexp.match(location_key):
            warnings.warn("incorrect location key - should satisfy [0-9a-zA-Z_]+", RuntimeWarning)
            return
        if not issubclass(location_class, Location):
            warnings.warn("location_class is not Location subclass: {class_}".format(
                class_=location_class.__name__
            ), RuntimeWarning)
            return

        _location = location_class(
            *args,
            loop=self._loop,
            income_queue=self._processing_queue,
            **kwargs
        )
        if _location not in self._locations:
            self._locations.append(_location)
            self._location_key_location_mapping[location_key] = _location
        else:
            warnings.warn("location is already in use", RuntimeWarning)

        return _location

    def embed(self):
        pass

    def _on_exception_engine_run(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Assembly"].error(
                "Catch exception", stage="Engine running",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )

    async def _processing(self):
        try:
            while True:
                ex_signal = await self._processing_queue.get()
        except asyncio.CancelledError:
            pass

    def _on_exception_processing(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Assembly"].error(
                "Catch exception", stage="Processing",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )

    def _on_exception_location(self, future):
        try:
            future.result()
        except asyncio.CancelledError:
            pass
        except Exception as ex:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            self.logger["Assembly"].error(
                "Catch exception", stage="Location",
                exception=str(ex), details="".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            )

    async def run(self):
        try:
            self._engine_future = asyncio.ensure_future(self._engine, loop=self._loop)
            self._engine_future.add_done_callback(self._on_exception_engine_run)

            self._processing_future = asyncio.ensure_future(self._processing(), loop=self._loop)
            self._processing_future.add_done_callback(self._on_exception_processing)

            for location in self._locations:
                future = asyncio.ensure_future(location.run(), loop=self._loop)
                future.add_done_callback(self._on_exception_location)
                self._location_futures.append(future)

            await self._engine.stopped.wait()
        except asyncio.CancelledError:
            pass
        finally:
            for location_future in self._location_futures:
                location_future.cancel()
            self._engine_future.cancel()
            self._processing_future.cancel()
            await self._engine.stopped.wait()
