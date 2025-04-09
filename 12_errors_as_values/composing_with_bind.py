# composing_with_bind.py
from pprint import pprint

from composing_functions import (
    func_a,
    func_b,
    func_c,
    func_d,
)
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


def composed(
    i: int,
) -> Result[str, str | ZeroDivisionError | ValueError]:
    # fmt: off
    return (
        func_a(i)
        .bind(func_b)
        .bind(func_c)
        .bind(func_d)
    )


pprint([(i, composed(i)) for i in range(5)])
## [(0, <Failure: division by zero>),
##  (1, <Failure: func_a(1)>),
##  (2, <Failure: func_b(2)>),
##  (3, <Failure: func_c(3): division by zero>),
##  (4, <Success: func_d(4)>)]
