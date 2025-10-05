import datetime
from logging import Formatter, LogRecord

import pytz

log_fmt: str = (
    "%(asctime)s::%(levelname)s::%(threadName)s::%(filename)s::"
    "%(funcName)s::%(lineno)d::%(name)s::%(message)s"
)
date_fmt: str = "%Y-%m-%d %H:%M:%S.%f"

EST = pytz.timezone("US/Eastern")


class CustomLogFormatter(Formatter):
    def formatTime(self, record: LogRecord, datefmt: str | None = None) -> str:  # noqa: N802, PLR6301
        ct = datetime.datetime.fromtimestamp(record.created).astimezone(EST)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = f"{t},{int(record.msecs):03d}"
        return s


def get_formatter() -> CustomLogFormatter:
    return CustomLogFormatter(fmt=log_fmt, datefmt=date_fmt)
