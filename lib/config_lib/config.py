from logging import Logger
from typing import Any

from lib.file_lib.file_factory import FileFactory
from lib.file_lib.json_tool import json_read, json_write


class ConfigurationBase:
    def __init__(
        self, filename: str | FileFactory, logger: Logger | None = None
    ) -> None:
        self._file = FileFactory(filename) if isinstance(filename, str) else filename
        self._logger = logger
        self.check_exists()

    def check_exists(self) -> bool:
        result: bool = False
        if self._file.exists():
            result = True
        else:
            if self._logger:
                self._logger.error("File: %s not found!", self._file)
            raise FileNotFoundError

        return result

    def get_extension(self) -> str:
        return self._file.suffix


class JsonConfiguration(ConfigurationBase):
    def __init__(
        self, filename: str | FileFactory, logger: Logger | None = None
    ) -> None:
        super().__init__(filename, logger)
        self.__configs: dict[str, Any] = {}
        self.is_json()

    def load_configs(self) -> None:
        self.__configs = json_read(self._file)

    def save_configs(self, configs: dict[Any, Any]) -> None:
        json_write(configs, self._file)

    def get_configs(self) -> dict[str, Any]:
        return self.__configs

    def is_json(self) -> None:
        if self.get_extension() != ".json":
            message: str = f"File: {self._file} is not a .json file."
            if self._logger:
                self._logger.error(message)
            raise OSError(message)
