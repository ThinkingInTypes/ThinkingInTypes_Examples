# discarded_state.py
# Exception throws everything away
from book_utils import Catch


def fa(i: int) -> int:
    if i == 1:
        raise ValueError(f"fa({i})")
    return i


with Catch():
    result = [fa(i) for i in range(3)]
    print(result)
## Error: fa(1)
