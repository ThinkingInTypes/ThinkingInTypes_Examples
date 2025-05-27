# composing_with_bind.py
from pprint import pprint
from returns.result import Result

from composing_functions import fa, fb, fc, fd


def composed(
    i: int,
) -> Result[str, str | ZeroDivisionError | ValueError]:
    # fmt: off
    return (
        # TODO: typing is incorrect & needs fixing
        fa(i)
        .bind(fb)  # type: ignore
        .bind(fc)  # type: ignore
        .bind(fd)  # type: ignore
    )


pprint([(i, composed(i)) for i in range(5)])
## [(0, <Failure: division by zero>),
##  (1, <Failure: fa(1)>),
##  (2, <Failure: fb(2)>),
##  (3, <Failure: fc(3): division by zero>),
##  (4, <Success: fd(1): 1>)]
