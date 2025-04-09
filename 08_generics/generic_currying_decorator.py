# generic_currying_decorator.py
from typing import Callable, TypeVar

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


def curry(
    func: Callable[[A, B], C],
) -> Callable[[A], Callable[[B], C]]:
    def outer(a: A) -> Callable[[B], C]:
        def inner(b: B) -> C:
            return func(a, b)

        return inner

    return outer


@curry
def multiply(x: int, y: int) -> int:
    return x * y


times_ten = multiply(10)
print(times_ten(3))
## 30
