"""
    Engine locations
"""

import asyncio


class Location(object):
    def __init__(self, *args, **kwargs):
        self._loop = kwargs.get("loop", asyncio.get_event_loop())
        self._income_queue = kwargs.get("income_queue", None)
        self._outcome_queue = asyncio.Queue(loop=self._loop)

    @property
    def outcome_queue(self):
        return self._outcome_queue

    async def run(self):
        raise NotImplementedError("run should be implemented in EngineLocation subclasses")


from comotore.locations.process_location import (ProcessLocation, InterprocessChannel)
