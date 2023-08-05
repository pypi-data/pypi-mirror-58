"""
    Timeout response
"""

from comotore.errors import Error


class ErrorTimeoutResponse(Error):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._code = "TIMEOUT_RESPONSE"
        self._text = "Timeout response"
