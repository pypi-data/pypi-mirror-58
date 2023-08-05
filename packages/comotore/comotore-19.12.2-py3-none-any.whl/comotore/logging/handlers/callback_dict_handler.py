"""
    Class logging callback dict handler
"""

import logging


class CallbackDictHandler(logging.Handler):
    def __init__(self, callback=None):
        logging.Handler.__init__(self)

        self.callback = callback

    def emit(self, record):
        if self.callback is not None:
            self.callback(self.formatter.format(record))
