# example_2.py
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")  # Declare a type variable


@dataclass
class Box(Generic[T]):
    content: T


box_int = Box(123)  # Box[int]
box_str = Box("hello")  # Box[str]
