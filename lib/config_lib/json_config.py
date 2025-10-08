from logging import Logger
from typing import Any

from lib.file_lib.file_factory import FileFactory
from lib.file_lib.json_tool import json_read, json_write


class ConfigurationBase:
    def __init__(self, filename: str | FileFactory, logger: Logger | None) -> None:
        self.file = FileFactory(filename) if isinstance(filename, str) else filename
        self.__logger = logger
        self.check_exists()

    def check_exists(self) -> bool:
        result: bool = False
        if self.file.exists():
            result = True
        else:
            if self.__logger:
                self.__logger.error("File: %s not found!", self.file)
            raise FileNotFoundError

        return result

    def get_extension(self) -> str:
        return self.file.suffix


class JsonConfiguration(ConfigurationBase):
    def __init__(self, filename: str | FileFactory, logger: Logger | None) -> None:
        super().__init__(filename, logger)
        self.configs: dict[str, Any] = {}

    def load_configs(self) -> dict[str, Any]:
        return json_read(self.file)

    def save_configs(self) -> None:
        json_write(self.configs, self.file)
