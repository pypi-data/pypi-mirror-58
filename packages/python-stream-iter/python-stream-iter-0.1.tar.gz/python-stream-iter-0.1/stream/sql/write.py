import typing as _typing

from . import (
    BaseDatabaseTable as _BaseDatabaseTable,
    Model as _Model,
)


class DatabaseTableWrite(_BaseDatabaseTable[_Model]):
    """
    Write access to a database table.
    """

    def truncate(self):
        try:
            self.engine.execute(f"TRUNCATE TABLE {self.model.__table__}")
        except Exception:
            self.get_query().delete()

    def bulk_insert(self, objects: _typing.Iterable[_Model]):
        self.session.add_all(objects)
