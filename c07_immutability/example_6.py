# example_6.py
from dataclasses import dataclass

from book_utils import Catch


@dataclass(frozen=True)
class Point:
    x: int
    y: int


p = Point(x=1, y=2)
print(p.x, p.y)  # Outputs: 1 2
## 1 2

with Catch():
    # Attempting to modify a field produces an error:
    p.x = 5  # type: ignore

p.__dict__["x"] = 5  # Bypassing 'frozen'
