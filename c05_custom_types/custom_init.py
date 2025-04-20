# custom_init.py
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float

    def __init__(self, coord: str):
        x_str, y_str = coord.split(",")
        self.x = float(x_str.strip())
        self.y = float(y_str.strip())


print(Point(" 10.5 , 20.3 "))
## Point(x=10.5, y=20.3)
