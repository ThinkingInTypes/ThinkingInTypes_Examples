# example_25.py
from box import Box
## 123
## Python

box: Box[int] = Box(123)
box.content = "not an int"  # type: ignore
