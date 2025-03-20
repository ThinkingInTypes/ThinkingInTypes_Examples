# example_2.py
from typing import Generic


class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content


box_int = Box(123)
box_str = Box("hello")
