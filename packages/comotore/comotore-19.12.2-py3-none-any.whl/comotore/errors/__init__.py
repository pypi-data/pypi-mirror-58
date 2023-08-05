"""
    Errors
"""


class Error(Exception):
    _code = None
    _text = None

    def __init__(self, message="", *args, **kwargs):
        self._message = message
        self._parameters = kwargs

        msg = "{text} {msg} ({parameters})".format(
                text=self._text,
                msg=message,
                parameters=",".join(["{key}={par}".format(
                    key=key,
                    par=self._parameters[key]) for key in self._parameters.keys()]
                )
            )

        super().__init__(msg)

    @property
    def text(self):
        if self._parameters is None:
            return self._text,
        else:
            return "{text} {msg} ({parameters})".format(
                text=self._text,
                msg=self._message,
                parameters=",".join(["{key}={par}".format(
                    key=key,
                    par=self._parameters[key]) for key in self._parameters.keys()]
                )
            )


from comotore.errors.error_timeout_response import ErrorTimeoutResponse
from comotore.errors.error_end_of_response import ErrorEndOfResponse
