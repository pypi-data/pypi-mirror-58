"""
    Process location
"""

import multiprocessing
import queue
import asyncio

from comotore.locations import Location


class InterprocessChannel(object):
    def __init__(self):
        self._is_reversed = False
        self._income_queue = multiprocessing.Queue()
        self._outcome_queue = multiprocessing.Queue()
        self._log_queue = multiprocessing.Queue()

    @property
    def reversed(self):
        channel = InterprocessChannel()
        self._is_reversed = True
        channel._outcome_queue = self._income_queue
        channel._income_queue = self._outcome_queue
        return channel

    @property
    def income(self):
        return self._income_queue

    @property
    def outcome(self):
        return self._outcome_queue

    @property
    def log(self):
        return self._log_queue


class ProcessLocation(Location):
    def __init__(self, channel, **kwargs):
        super().__init__(**kwargs)

        self._channel = channel

    async def _income_processing(self):
        try:
            while True:
                try:
                    message = self._channel.income.get_nowait()
                    if self._income_queue is not None:
                        await self._income_queue.put(message)
                except queue.Empty:
                    pass
                await asyncio.sleep(0.005)
        except asyncio.CancelledError:
            pass

    async def _outcome_processing(self):
        try:
            while True:
                message = await self._outcome_queue.get()
                self._channel.outcome.put(message)
        except asyncio.CancelledError:
            pass

    async def run(self):
        income_processing_future = None
        outcome_processing_future = None
        try:
            income_processing_future = asyncio.ensure_future(self._income_processing())
            outcome_processing_future = asyncio.ensure_future(self._outcome_processing())
        except asyncio.CancelledError:
            pass
        finally:
            income_processing_future.cancel()
            outcome_processing_future.cancel()
