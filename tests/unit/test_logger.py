import logging
import re
import sys
from pathlib import Path
from typing import TextIO

import pytest

from lib.file_lib.file_factory import FileFactory
from lib.logger_lib import log_formatter, logger

# pylint: disable-next=unused-import
from tests.test_fixtures import common_file_factory_fixture


def test_basic_logger(common_file_factory_fixture_: FileFactory) -> None:
    file_f: FileFactory = common_file_factory_fixture_
    logger_name: str = "TestLogger"
    log_level: int = logging.INFO
    test_logger: logging.Logger = logger.get_logger(logger_name, log_level, str(file_f))
    assert test_logger.level is logging.INFO
    log_msg: str = "This is a test log"
    test_logger.debug(log_msg)
    assert not file_f.read()

    test_logger.info(log_msg)
    matchstr = (
        rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}}\.\d+::"
        rf"{logging.getLevelName(log_level)}::MainThread::"
        rf"{Path(__file__).name}::{test_basic_logger.__name__}::"
        rf"\d+::{logger_name}::{log_msg}"
    )
    assert re.match(matchstr, file_f.read())


def test_basic_logger_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    logger_name: str = "TestStdoutLogger"
    log_level: int = logging.INFO
    # No logfile provided - should use stdout
    test_logger: logging.Logger = logger.get_logger(logger_name, log_level, None)
    assert test_logger.level is logging.INFO

    log_msg: str = "This is a stdout test log"
    test_logger.info(log_msg)

    captured = capsys.readouterr()
    matchstr = (
        rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}}\.\d+::"
        rf"{logging.getLevelName(log_level)}::MainThread::"
        rf"{Path(__file__).name}::{test_basic_logger_stdout.__name__}::"
        rf"\d+::{logger_name}::{log_msg}"
    )
    assert re.match(matchstr, captured.out.strip())


def test_log_formatter_no_date_fmt(capsys: pytest.CaptureFixture[str]) -> None:
    logger_name: str = "TestFmtLogger"
    log_level: int = logging.DEBUG
    test_logger: logging.Logger = logging.getLogger(logger_name)
    test_logger.setLevel(log_level)
    assert test_logger.level is logging.DEBUG
    formatter: logging.Formatter = log_formatter.CustomLogFormatter(
        fmt=log_formatter.LOG_FMT
    )
    sh: logging.StreamHandler[TextIO] = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    test_logger.addHandler(sh)

    log_msg: str = "This is a stdout test log"
    test_logger.debug(log_msg)

    captured = capsys.readouterr()
    matchstr = (
        rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}}:\d{{2}}\.\d+::"
        rf"{logging.getLevelName(log_level)}::MainThread::"
        rf"{Path(__file__).name}::{test_log_formatter_no_date_fmt.__name__}::"
        rf"\d+::{logger_name}::{log_msg}"
    )
    assert re.match(matchstr, captured.out.strip())
