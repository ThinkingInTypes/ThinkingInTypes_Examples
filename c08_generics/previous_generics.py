# previous_generics.py
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]): ...
