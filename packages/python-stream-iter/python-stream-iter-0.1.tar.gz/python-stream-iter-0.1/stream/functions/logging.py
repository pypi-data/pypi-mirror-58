from stream.mixins.logging import (
    LogFunc as _LogFunc,
    Formatter as _Formatter,
    LogItemFunc as _LogItemFunc,
)
from stream.mixins.match import (
    Match as _Match,
    MatchFunc as _MatchFunc,
)
from stream.typing import (
    T_co as _T_co,
)
from .conditional import (
    BaseApplyIf as _BaseApplyIf,
)


class LogIf(
    _BaseApplyIf[_T_co, _T_co],
    _MatchFunc[_T_co],
    _LogItemFunc[_T_co],
):
    def __init__(
            self,
            match: _Match,
            log_func: _LogFunc,
            formatter: _Formatter = str,
    ):
        _MatchFunc.__init__(self, match)
        _LogItemFunc.__init__(self, log_func, formatter)

    def each(self, item: _T_co) -> _T_co:
        self.log(item)
        return item
