# generic_method_in_protocol.py
from typing import Protocol, TypeVar

T = TypeVar("T")


class Container(Protocol):
    def get_item(self, type_: type[T]) -> T: ...
