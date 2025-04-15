# example_12.py
from typing import ParamSpec, Callable, Concatenate

P = ParamSpec("P")


def make_logged(
        func: Callable[P, int],
) -> Callable[Concatenate[str, P], int]:
    def wrapper(
            prefix: str, *args: P.args, **kwargs: P.kwargs
    ) -> int:
        print(prefix, "Calling:", func.__name__)
        result = func(*args, **kwargs)
        print(prefix, "Result:", result)
        return result

    return wrapper
