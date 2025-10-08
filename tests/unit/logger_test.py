import logging
import re
from pathlib import Path

import pytest

from lib.file_lib.file_factory import FileFactory
from lib.logger_lib import logger

# pylint: disable-next=unused-import
from lib.test_lib.test_fixures import common_file_factory_fixture


def test_basic_logger(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    logger_name: str = "TestLogger"
    log_level: int = logging.INFO
    test_logger: logging.Logger = logger.get_logger(logger_name, log_level, str(file_f))
    assert test_logger.level is logging.INFO
    log_msg: str = "This is a test log"
    # NOTE: Should not write as in INFO
    test_logger.debug(log_msg)
    assert not file_f.read()

    test_logger.info(log_msg)
    matchstr = (
        rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}}\.\d+::"
        rf"{logging.getLevelName(log_level)}::MainThread::"
        rf"{Path(__file__).name}::{test_basic_logger.__name__}::"
        rf"\d+::{logger_name}::{log_msg}"
    )
    assert re.search(matchstr, file_f.read())


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main())
