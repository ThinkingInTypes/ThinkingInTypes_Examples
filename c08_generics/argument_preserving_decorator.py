# argument_preserving_decorator.py
from typing import Callable

def log_call[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
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
## Calling greet with args=('Alice', 30),
## kwargs={}
## Hi Alice, age 30
print(add(2, 3))
## Calling add with args=(2, 3), kwargs={}
## 5
