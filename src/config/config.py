from pathlib import Path


class Configuration:
    def __init__(self, filename: str | Path) -> None:
        """Instantiate with filename"""
        self.filename: str | Path = filename
