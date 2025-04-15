# composing_with_bind.py
from pprint import pprint
from returns.result import Result

from composing_functions import (
    func_a,
    func_b,
    func_c,
    func_d,
)


def composed(
        i: int,
) -> Result[str, str | ZeroDivisionError | ValueError]:
    # fmt: off
    return (
        # TODO: this is incorrect & needs fixing
        func_a(i)
        .bind(func_b)  # type: ignore
        .bind(func_c)  # type: ignore
        .bind(func_d)  # type: ignore
    )


pprint([(i, composed(i)) for i in range(5)])
