# discarded_state.py
# Exception throws everything away
from book_utils import Catch


def func_a(i: int) -> int:
    if i == 1:
        raise ValueError(f"func_a({i})")
    return i


with Catch():
    result = [func_a(i) for i in range(3)]
    print(result)
## Error: func_a(1)
