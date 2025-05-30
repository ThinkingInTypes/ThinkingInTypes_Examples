# multiple_arguments.py
from pprint import pprint

from composing_functions import fa, fb, fc
from returns.result import Result


def add(first: int, second: int, third: int) -> str:
    return f"add({first} + {second} + {third}): {first + second + third}"


def composed(
    i: int, j: int
) -> Result[str, str | ZeroDivisionError | ValueError]:
    # fmt: off
    return Result.do(
        add(first, second, third)
        for first in fa(i)
        for second in fb(j)
        for third in fc(i + j)
    )


inputs = [(1, 5), (7, 2), (2, 1), (7, 5)]
pprint([(args, composed(*args)) for args in inputs])
## [((1, 5), <Failure: fa(1)>),
##  ((7, 2), <Failure: fb(2)>),
##  ((2, 1), <Failure: fc(3): division by zero>),
##  ((7, 5), <Success: add(7 + 5 + 0): 12>)]
