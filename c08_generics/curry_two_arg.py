# curry_two_arg.py
from typing import Callable


def curry_two_arg[X, Y, Z](
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
# get_double is now Callable[[float], float]:
get_double = curried_mul(2)
print(get_double(3.5))
## 7.0
