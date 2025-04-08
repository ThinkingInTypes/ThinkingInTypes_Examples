# return_result.py
# Result type returns Success/Failure
# Using https://github.com/dry-python/returns
from pprint import pprint

from returns.result import Failure, Result, Success


def func_a(i: int) -> Result[int, str]:
    if i == 1:
        return Failure(f"func_a({i})")
    return Success(i)


pprint([(i, func_a(i)) for i in range(5)])
## [(0, <Success: 0>),
##  (1, <Failure: func_a(1)>),
##  (2, <Success: 2>),
##  (3, <Success: 3>),
##  (4, <Success: 4>)]
