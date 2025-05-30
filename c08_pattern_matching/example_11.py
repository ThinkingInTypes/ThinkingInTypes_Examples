# example_11.py
from typing_extensions import NamedTuple


class Circle(NamedTuple):
    radius: float


class Square(NamedTuple):
    side: float


def shape_area(shape: Circle | Square) -> float:
    match shape:
        case Circle(radius=r):
            # Here shape is type Circle:
            return 3.14 * r**2
        case Square(side=s):
            # Here shape is type Square:
            return s**2
        case _:
            raise ValueError("Unsupported shape")
