# example_6.py
from typing import Protocol, TypeVar

T = TypeVar("T")


class Container(Protocol[T]):
    def get_item(self) -> T: ...
