# vector.py

type Vector[T] = list[tuple[T, T]]


def scale_points(points: Vector[int], factor: int) -> Vector[int]:
    return [(x * factor, y * factor) for (x, y) in points]
