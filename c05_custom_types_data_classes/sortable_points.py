# sortable_points.py
from point_dataclasses import OrderedPoint

ordered_points: list[OrderedPoint] = [
    OrderedPoint(3, 4),
    OrderedPoint(1, 9),
    OrderedPoint(1, 2),
]
print(sorted(ordered_points))
## [OrderedPoint(x=1, y=2), OrderedPoint(x=1, y=9),
## OrderedPoint(x=3, y=4)]
