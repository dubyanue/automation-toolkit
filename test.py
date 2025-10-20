from lib.dbc_lib import dbc_utils
from lib.dbc_lib.dbc import SQLite
from lib.file_lib.file_factory import FileFactory
from lib.logger_lib.logger import get_logger

logger = get_logger(__file__)
ff = FileFactory("/logs/work/data/tests/data/test.db")
sqlfile = FileFactory("/logs/work/data/tests/data/test.sql")
criteria: list[str] | None = None
query_kwargs: dbc_utils.QueryKwargs = dbc_utils.QueryKwargs(None, criteria, None)

sql = SQLite(logger=logger)
with sqlfile.open("r") as fh:
    sql.executescript(fh.read())

sql2 = SQLite(ff, logger)
sql2.connect()
if sql2.cnxn:
    sql.backup(sql2.cnxn)
