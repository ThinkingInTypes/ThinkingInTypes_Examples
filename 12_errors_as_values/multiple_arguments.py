# multiple_arguments.py
from pprint import pprint

from composing_functions import func_a, func_b, func_c
## [(0, <Success: 0>),
##  (1, <Failure: func_a(1)>),
##  (2, <Success: 2>),
##  (3, <Success: 3>),
##  (4, <Success: 4>)]
## [(0, <Failure: division by zero>),
##  (1, <Failure: func_a(1)>),
##  (2, <Failure: func_b(2)>),
##  (3, <Failure: func_c(3): division by zero>),
##  (4, <Success: func_d(4)>)]
from returns.result import Result


def add(first: int, second: int, third: int) -> str:
    return f"add({first} + {second} + {third}):" f" {first + second + third}"


def composed(i: int, j: int) -> Result[str, str | ZeroDivisionError | ValueError]:
    # fmt: off
    return Result.do(
        add(first, second, third)
        for first in func_a(i)
        for second in func_b(j)
        for third in func_c(i + j)
    )


inputs = [(1, 5), (7, 2), (2, 1), (7, 5)]
pprint([(args, composed(*args)) for args in inputs])
## [((1, 5), <Failure: func_a(1)>),
##  ((7, 2), <Failure: func_b(2)>),
##  ((2, 1), <Failure: func_c(3): division by
## zero>),
##  ((7, 5), <Success: add(7 + 5 + 12): 24>)]
