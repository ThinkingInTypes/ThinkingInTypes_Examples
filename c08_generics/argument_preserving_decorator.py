# argument_preserving_decorator.py
from typing import Callable, ParamSpec, TypeVar, TypeVarTuple, Unpack

P = ParamSpec("P")
R = TypeVar("R")


def log_call(fn: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {fn.__name__} with {args=}, {kwargs=}")
        return fn(*args, **kwargs)

    return wrapper


@log_call
def greet(name: str, age: int) -> str:
    return f"Hi {name}, age {age}"


@log_call
def add(a: int, b: int) -> int:
    return a + b


print(greet("Alice", 30))
print(add(2, 3))
