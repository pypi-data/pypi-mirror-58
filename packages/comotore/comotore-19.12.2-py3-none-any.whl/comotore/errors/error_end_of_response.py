"""
    End of response
"""

from comotore.errors import Error


class ErrorEndOfResponse(Error):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._code = "END_OF_RESPONSE"
        self._text = "End of response"
