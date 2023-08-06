from sqlalchemy.orm import (
    Query as _Query,
)

from stream import (
    Stream as _Stream,
    IterStream as _IterStream,
)
from . import (
    BaseDatabaseTable as _BaseDatabaseTable,
    Model as _Model,
)


class DatabaseTableRead(_BaseDatabaseTable[_Model]):
    """
    Read access to a database table.

    Before calling `.stream`,
    the query can be customized by assigning to `.query`.
    Use `.get_query()` to get the initial query.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__query = None

    @property
    def query(self) -> _Query:
        if self.__query is None:
            self.__query = self.get_query()
        return self.__query

    @query.setter
    def query(self, val: _Query):
        self.__query = val

    @property
    def stream(self) -> _Stream[_Model]:
        return _IterStream(self.query)
