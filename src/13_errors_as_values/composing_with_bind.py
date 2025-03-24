# composing_with_bind.py
from pprint import pprint

from composing_functions import func_a, func_b, func_c, func_d
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
