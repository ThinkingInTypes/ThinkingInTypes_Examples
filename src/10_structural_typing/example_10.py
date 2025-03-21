# example_10.py
from typing import Protocol


class Container(Protocol):
    def get_item[T](self) -> T: ...
