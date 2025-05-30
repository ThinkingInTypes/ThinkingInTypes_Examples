# hashable_points.py
from point_dataclasses import FrozenPoint

point_set: set[FrozenPoint] = {
    FrozenPoint(1, 2),
    FrozenPoint(3, 4),
}
print(FrozenPoint(1, 2) in point_set)
## True
point_dict: dict[FrozenPoint, str] = {
    FrozenPoint(1, 2): "first",
    FrozenPoint(3, 4): "second",
}
print(point_dict[FrozenPoint(3, 4)])
## second
