# generic_method_in_protocol.py
from typing import Protocol


class Container(Protocol):
    def get_item[T](self) -> T: ...
