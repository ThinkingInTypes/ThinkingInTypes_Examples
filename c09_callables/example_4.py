# example_4.py
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def logging_decorator(
    func: Callable[P, R],
) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logging_decorator
def multiply(a: int, b: int) -> int:
    return a * b


multiply(2, 3)  # Output: Calling multiply with (2, 3) and {} then returns 6
## Calling multiply with (2, 3) and {}
