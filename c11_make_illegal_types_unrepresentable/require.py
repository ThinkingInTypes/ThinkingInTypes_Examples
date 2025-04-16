# require.py
from typing import Callable, NamedTuple
from functools import wraps


class Condition(NamedTuple):
    check: Callable[..., bool]
    message: str


def requires(*conditions: Condition):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for condition in conditions:
                if not condition.check(
                        *args, **kwargs
                ):
                    raise ValueError(condition.message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
