# asdict_behavior.py
from dataclasses import dataclass, asdict

from point_dataclasses import Point


@dataclass
class Line:
    p1: Point
    p2: Point


@dataclass
class Shape:
    lines: list[Line]


@dataclass
class Image:
    shapes: list[Shape]


shape1 = Shape(
    [
        Line(Point(0, 0), Point(10, 4)),
        Line(Point(10, 4), Point(16, 8)),
    ]
)

image = Image([shape1, shape1])
print(image.__dict__)
## {'shapes': [Shape(lines=[Line(p1=Point(x=0, y=0), p2=Point(x=10,
## y=4)), Line(p1=Point(x=10, y=4), p2=Point(x=16, y=8))]),
## Shape(lines=[Line(p1=Point(x=0, y=0), p2=Point(x=10, y=4)),
## Line(p1=Point(x=10, y=4), p2=Point(x=16, y=8))])]}
print(asdict(image))
## {'shapes': [{'lines': [{'p1': {'x': 0, 'y': 0}, 'p2': {'x': 10,
## 'y': 4}}, {'p1': {'x': 10, 'y': 4}, 'p2': {'x': 16, 'y': 8}}]},
## {'lines': [{'p1': {'x': 0, 'y': 0}, 'p2': {'x': 10, 'y': 4}},
## {'p1': {'x': 10, 'y': 4}, 'p2': {'x': 16, 'y': 8}}]}]}
