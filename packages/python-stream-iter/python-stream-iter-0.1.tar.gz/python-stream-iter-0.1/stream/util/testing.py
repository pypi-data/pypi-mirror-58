from contextlib import (
    contextmanager as _contextmanager,
)
from time import (
    time as _time,
)


@_contextmanager
def assert_time(
        expected_time,
        *,
        margin=0.02,
):
    start = _time()
    try:
        yield
    finally:
        t = _time() - start
        assert -margin <= t - expected_time <= margin
