from stream.functions.filter import (
    Filter as _Filter,
    remove_empty as _remove_empty,
)
from . import (
    from_function as _from_function,
)

filter_ = _from_function(_Filter, has_params=True)
remove_empty = _from_function(_remove_empty, has_params=False)
