# example_8.py
from typing import Callable, TypeVar

X = TypeVar("X")
Y = TypeVar("Y")
Z = TypeVar("Z")


def curry_two_arg(
    func: Callable[[X, Y], Z],
) -> Callable[[X], Callable[[Y], Z]]:
    def curried(x: X) -> Callable[[Y], Z]:
        def inner(y: Y) -> Z:
            return func(x, y)

        return inner

    return curried


def multiply(a: int, b: float) -> float:
    return a * b


curried_mul = curry_two_arg(multiply)
get_double = curried_mul(
    2
)  # get_double is now Callable[[float], float]
result = get_double(3.5)  # result = 7.0
