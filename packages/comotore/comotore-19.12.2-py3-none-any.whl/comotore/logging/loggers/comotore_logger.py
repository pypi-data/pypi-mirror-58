"""
    Runnable logger
"""

import logging
import platform


class ComotoreLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super(ComotoreLogger, self).__init__(name, level)

        self._hostname = platform.uname()[1]
        self._current_tag = None

    def __getitem__(self, tag):
        self._current_tag = tag
        return self

    def _reset_tag(self):
        self._current_tag = None

    def _prepare(self, **kwargs):
        exc_info = kwargs.get("exc_info", None)
        extra = kwargs.get("extra", {})
        stack_info = kwargs.get("stack_info", False)

        if self._current_tag is None:
            extra["tag"] = ""
        else:
            extra["tag"] = self._current_tag
        extra["hostname"] = self._hostname

        data = {}
        for key in kwargs:
            if key not in ["exc_info", "extra", "stack_info", "tag"]:
                data[key] = kwargs.get(key)
        extra["data"] = data

        return exc_info, extra, stack_info

    def debug(self, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).debug(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def info(self, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).info(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def warning(self, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).warning(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def error(self, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).error(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).exception(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def critical(self, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).exception(msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)

    def log(self, level, msg, *args, **kwargs):
        exc_info, extra, stack_info = self._prepare(**kwargs)
        self._reset_tag()
        super(ComotoreLogger, self).log(level, msg, *args, exc_info=exc_info, extra=extra, stack_info=stack_info)
