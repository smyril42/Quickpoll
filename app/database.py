from sqlite3 import connect, Row
from pathlib import Path
from os.path import split as path_split


__all__ = "SQLiteHandler", "db_init"


class SQLiteHandler:
    """
    how to connect to sqlite database:

    # # #
    with SQLiteHandler(path) as cur:
        # cur.execute(command)
        ...
    # # #

    will commit and close the connection automatically
    """
    def __init__(self, file, row=True):
        self.file = file
        self.row = row

    def __enter__(self):
        self.conn = connect(self.file)
        if self.row:
            self.conn.row_factory = lambda *args, **kwargs: dict(Row(*args, **kwargs))
        return self.conn.cursor()

    def __exit__(self, err_type, value, traceback):
        self.conn.commit()
        self.conn.close()


def db_init(path, schema):
    Path(path_split(path)[0]).mkdir(parents=True, exist_ok=True)

    with open(schema, "rt", encoding="utf-8") as f:
        structure = f.read()

    with SQLiteHandler(path) as cur:
        cur.executescript(structure)
