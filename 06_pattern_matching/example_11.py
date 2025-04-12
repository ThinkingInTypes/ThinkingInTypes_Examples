# example_11.py
from typing_extensions import NamedTuple


class Circle(NamedTuple):
    radius: float


class Square(NamedTuple):
    side: float


def shape_area(shape: Circle | Square) -> float:
    match shape:
        case Circle(radius=r):
            ...  # here shape is type Circle
        case Square(side=s):
            ...  # here shape is type Square
