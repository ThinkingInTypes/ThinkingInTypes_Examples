# require.py
from dataclasses import dataclass
from typing import Callable
from functools import wraps


@dataclass(frozen=True)
class Condition:
    check: Callable[..., bool]
    message: str


def requires(*conditions: Condition):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for condition in conditions:
                if not condition.check(*args, **kwargs):
                    raise ValueError(condition.message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
