from typing import Any

import pytest

from lib.config_lib import config
from lib.file_lib.file_factory import FileFactory
from lib.logger_lib.logger import get_logger

# pylint: disable-next=unused-import
from tests.test_fixtures import (
    common_file_factory_fixture,
    json_database_config_fixture,
    json_file_factory_fixture,
)


def test_raise_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        config.ConfigurationBase(
            "test.json", get_logger(test_raise_file_not_found.__name__)
        )

    with pytest.raises(FileNotFoundError):
        config.ConfigurationBase("test.json")


def test_file_exists(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    file_f, _, _ = json_file_factory_fixture_
    config_base: config.ConfigurationBase = config.ConfigurationBase(file_f)
    assert config_base.check_exists() is True


def test_file_extension(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    file_f, _, _ = json_file_factory_fixture_
    config_base: config.ConfigurationBase = config.ConfigurationBase(file_f)
    assert config_base.get_extension() == ".json"


def test_save_load_json_config(
    json_file_factory_fixture_: tuple[FileFactory, str, dict[str, Any]],
) -> None:
    file_f, _, test_dict = json_file_factory_fixture_
    json_config: config.JsonConfiguration = config.JsonConfiguration(file_f)
    json_config.save_configs(test_dict)
    json_config.load_configs()
    assert json_config.get_configs() == test_dict


def test_json_config_without_json_file(
    common_file_factory_fixture_: FileFactory,
) -> None:
    file_f: FileFactory
    file_f = common_file_factory_fixture_
    with pytest.raises(OSError, match=r"File:.* is not a \.json file\."):
        config.JsonConfiguration(file_f)
    with pytest.raises(OSError, match=r"File:.* is not a \.json file\."):
        config.JsonConfiguration(
            file_f, get_logger(test_json_config_without_json_file.__name__)
        )


def test_json_database_config(
    json_database_config_fixture_: config.JsonDatabaseConfiguration,
) -> None:
    jdc: config.JsonDatabaseConfiguration
    jdc = json_database_config_fixture_
    assert jdc.username == "user1"
    assert jdc.password == "pass1"
    assert jdc.server == "server1"
    assert jdc.driver == "driver1"
    assert jdc.database == "database1"
