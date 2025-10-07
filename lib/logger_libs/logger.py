import logging
import pathlib
import sys

from lib.logger_libs.log_formatter import get_formatter


class BasicLogger(logging.Logger):
    def __init__(
        self, name: str, level: int = logging.DEBUG, logfile: str | None = None
    ) -> None:
        super().__init__(name=name, level=level)

        formatter = get_formatter()

        if not logfile:
            sh = logging.StreamHandler(sys.stdout)
            sh.setFormatter(formatter)
            self.addHandler(sh)
        else:
            fh = logging.FileHandler(pathlib.Path(logfile).expanduser())
            fh.setFormatter(formatter)
            self.addHandler(fh)

        self.setLevel(self.level)


def get_logger(
    name: str, level: int = logging.DEBUG, logfile: str | None = None
) -> BasicLogger:
    return BasicLogger(name, level, logfile)
