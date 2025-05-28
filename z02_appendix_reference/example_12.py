# example_12.py
from typing import Callable


def make_logged[**P](
        func: Callable[P, int],
) -> Callable[..., int]:
    def wrapper(
            prefix: str, *args: P.args, **kwargs: P.kwargs
    ) -> int:
        print(f"{prefix} Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{prefix} Result: {result}")
        return result

    return wrapper


@make_logged
def add(x: int, y: int) -> int:
    return x + y


add("[LOG]", 3, 4)
## [LOG] Calling: add
## [LOG] Result: 7
