"""
    Class plain log formatter
"""

from logging import Formatter


class PlainFormatter(Formatter):
    def format(self, record):
        if hasattr(record, "data") and isinstance(record.data, (dict,)):
            if len(record.data) > 0:
                joined_data = ", ".join(["{key}={value}".format(key=k, value=record.data[k]) for k in record.data])
                record.data = "({data})".format(data=joined_data)
            else:
                record.data = ""
        return super().format(record)
