# example_4.py
from typing import Callable


def logging_decorator[**P, R](
        func: Callable[P, R],
) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(
            f"Calling {func.__name__} with {args} and {kwargs}"
        )
        return func(*args, **kwargs)

    return wrapper


@logging_decorator
def multiply(a: int, b: int) -> int:
    return a * b


multiply(2, 3)
## Calling multiply with (2, 3) and {}
