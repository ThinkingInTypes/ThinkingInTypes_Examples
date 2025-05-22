# return_result.py
# Result type returns Success/Failure
# Using https://github.com/dry-python/returns
from returns.result import Failure, Result, Success


def fa(i: int) -> Result[int, str]:
    if i == 1:
        return Failure(f"fa({i})")
    return Success(i)
