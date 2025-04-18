# post_init.py
from dataclasses import dataclass
from math import pi


@dataclass
class Circle:
    radius: float
    area: float = 0.0

    def __post_init__(self):
        self.area = pi * self.radius ** 2


print(Circle(radius=5))
