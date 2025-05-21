# composing_functions.py
from pprint import pprint

from return_result import func_a
from returns.result import (
    Failure,
    Result,
    Success,
    safe,
)


# Use an exception as info (but don't raise it):
def func_b(i: int) -> Result[int, ValueError]:
    if i == 2:
        return Failure(ValueError(f"func_b({i})"))
    return Success(i)


# Convert exception to Failure:
def func_c(i: int) -> Result[int, ZeroDivisionError]:
    try:
        j = int(1 / (i - 3))
    except ZeroDivisionError as e:
        return Failure(ZeroDivisionError(f"func_c({i}): {e}"))
    return Success(j)


@safe  # Convert existing function
def func_d(
    i: int,
) -> str:  # Result[str, ZeroDivisionError]
    j = int(1 / i)
    return f"func_d({i}): {j}"


def composed(
    i: int,
) -> Result[str, str | ValueError | ZeroDivisionError]:
    result_a = func_a(i)
    if isinstance(result_a, Failure):
        return result_a  # type: ignore

    # unwrap() gets the answer from Success:
    result_b = func_b(result_a.unwrap())
    if isinstance(result_b, Failure):
        return result_b  # type: ignore

    result_c = func_c(result_b.unwrap())
    if isinstance(result_c, Failure):
        return result_c  # type: ignore

    return func_d(result_c.unwrap())  # type: ignore
