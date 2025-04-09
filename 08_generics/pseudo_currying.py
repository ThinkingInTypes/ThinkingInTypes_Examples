# pseudo_currying.py
from functools import partial


def add(x: int, y: int) -> int:
    return x + y


add_five = partial(add, 5)
print(add_five(3))
## 8
