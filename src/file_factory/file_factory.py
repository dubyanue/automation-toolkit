from pathlib import Path


class FileFactory:
    def __init__(self, filename: str) -> None:
        self.__filename: str = filename
        self.__file_path: Path = Path(self.__filename)

    def get_path(self) -> Path:
        return self.__file_path
