from stream.functions.control import (
    Preload as _Preload,
)
from . import (
    from_function as _from_function,
)

preload = _from_function(_Preload, has_params=True)
