# dataclass_as_dict.py
from dataclasses import dataclass, asdict
from point_dataclasses import Point

p = Point(7, 9)
print(asdict(p))
## {'x': 7, 'y': 9}
print(p.__dict__)
## {'x': 7, 'y': 9}
# Unpacking:
x, y = tuple(asdict(p).values())
print(x, y)
## 7 9
# Or:
x1, y1 = tuple(p.__dict__.values())
print(x1, y1)
## 7 9
