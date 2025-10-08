from collections.abc import Generator
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from lib.file_lib.file_factory import FileFactory


@pytest.fixture(name="common_file_factory_fixture_")
def common_file_factory_fixture() -> Generator[FileFactory]:
    with NamedTemporaryFile(mode="w+", delete=False, encoding="utf-8") as tmp:
        filename_: str = tmp.name

    file_factory_: FileFactory = FileFactory(filename_)
    yield file_factory_

    if (file_path := Path(filename_)).exists():
        file_path.unlink(missing_ok=True)
