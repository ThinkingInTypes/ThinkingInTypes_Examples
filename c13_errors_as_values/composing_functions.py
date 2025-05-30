# composing_functions.py
from pprint import pprint

from return_result import fa
from returns.result import (
    Failure,
    Result,
    Success,
    safe,
)


# Use an exception as info (but don't raise it):
def fb(i: int) -> Result[int, ValueError]:
    if i == 2:
        return Failure(ValueError(f"fb({i})"))
    return Success(i)


# Convert exception to Failure:
def fc(i: int) -> Result[int, ZeroDivisionError]:
    try:
        j = int(1 / (i - 3))
    except ZeroDivisionError as e:
        return Failure(ZeroDivisionError(f"fc({i}): {e}"))
    return Success(j)


@safe  # Convert existing function
def fd(
    i: int,
) -> str:  # Result[str, ZeroDivisionError]
    j = int(1 / i)
    return f"fd({i}): {j}"


def composed(
    i: int,
) -> Result[str, str | ValueError | ZeroDivisionError]:
    result_a = fa(i)
    if isinstance(result_a, Failure):
        return result_a  # type: ignore

    # unwrap() gets the answer from Success:
    result_b = fb(result_a.unwrap())
    if isinstance(result_b, Failure):
        return result_b  # type: ignore

    result_c = fc(result_b.unwrap())
    if isinstance(result_c, Failure):
        return result_c  # type: ignore

    return fd(result_c.unwrap())  # type: ignore
