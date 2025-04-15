# example_23.py
from typing import TypeVar

T = TypeVar('T')
Vector = list[tuple[T, T]]


def scale_points(points: Vector[int], factor: int) -> Vector[int]:
    return [(x * factor, y * factor) for (x, y) in points]
