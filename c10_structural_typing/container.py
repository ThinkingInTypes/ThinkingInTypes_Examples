# container.py
from typing import Protocol


class Container[T](Protocol):
    def get_item(self) -> T: ...
