import typing as _typing

from gimme_cached_property import cached_property
from sqlalchemy.engine import (
    Engine as _Engine,
    create_engine as _create_engine,
)
from sqlalchemy.engine.url import (
    URL as _Url,
)
from sqlalchemy.ext.declarative.api import (
    DeclarativeMeta as _DeclarativeMeta,
)
from sqlalchemy.orm import (
    Query as _Query,
)
from sqlalchemy.orm import (
    Session as _Session,
    sessionmaker as _sessionmaker,
)

Model = _typing.TypeVar('Model', bound=_DeclarativeMeta)


class BaseDatabaseTable(_typing.Generic[Model]):
    class SessionStateError(Exception):
        pass

    def __init__(
            self,
            model: _typing.Type[Model],
            *,
            engine: _typing.Union[_Engine, _Url, str],
            session: _Session = None,
    ):
        """
        :param model: SqlAlchemy model
        :param engine:
            If an engine object, use it;
            If a str or an URL object, call create_engine.
        :param session:
            If provided, use the session for transactions;
            If None, `with` must be used - a session will be created in the context.
        """
        self.__model = model

        if isinstance(engine, (_Url, str)):
            engine = _create_engine(engine)
        self.__engine = engine

        self.__session = session
        self.__create_session = session is None

    @property
    def model(self) -> _typing.Type[Model]:
        return self.__model

    @property
    def engine(self) -> _Engine:
        return self.__engine

    @property
    def session(self) -> _Session:
        if self.__session is None:
            raise self.SessionStateError(
                'Please use `with` context manager when `session` is not provided'
            )
        return self.__session

    @cached_property
    def _session_class(self) -> _sessionmaker:
        return _sessionmaker(bind=self.engine)

    def get_query(self, *fields) -> _Query:
        if len(fields) == 0:
            return self.session.query(self.model)
        else:
            return self.session.query(*fields)

    def commit(self):
        self.session.commit()

    def __enter__(self) -> 'BaseDatabaseTable[Model]':
        if self.__create_session:
            if self.__session is not None:
                raise self.SessionStateError(
                    'Please do not use `with` context manager multiple times. '
                    'You may call `.commit()` within the `with` context.'
                )
            self.__session = self._session_class()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        if self.__create_session:
            self.session.close()
            self.__session = None
