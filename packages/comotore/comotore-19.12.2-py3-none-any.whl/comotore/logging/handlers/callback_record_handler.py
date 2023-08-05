"""
    Class logging callback record handler
"""

import logging


class CallbackRecordHandler(logging.Handler):
    def __init__(self, callback=None):
        logging.Handler.__init__(self)

        self.callback = callback

    def emit(self, record):
        if self.callback is not None:
            self.callback(record)
