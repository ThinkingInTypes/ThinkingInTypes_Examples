# dataclass_pattern_matching.py
from dataclasses import dataclass
from typing import Any


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Rectangle:
    width: int
    height: int
    color: str

    __match_args__ = (
        "width",
        "height",
    )  # control positional matching


def match_point(value: Any) -> None:
    match value:
        case Point(0, 0):
            print("Origin")
        case Point(x, 0):
            print(f"On X-axis at {x = }")
        case Point(0, y):
            print(f"On Y-axis at {y = }")
        case Point(x, y):
            print(f"General point: ({x}, {y})")
        case _:
            print("Not a Point")


def match_rectangle(value: Any) -> None:
    match value:
        case Rectangle(
            100, 200
        ):  # uses __match_args__: width, height
            print("Large rectangle")
        case Rectangle(width=w, height=h, color=c):
            print(f"Rectangle: width={w}, height={h}, color={c}")
        case _:
            print("Not a Rectangle")


match_point(Point(0, 0))
## Origin
match_point(Point(5, 0))
## On X-axis at x = 5
match_point(Point(0, 7))
## On Y-axis at y = 7
match_point(Point(3, 4))
## General point: (3, 4)
match_point(None)
## Not a Point
match_rectangle(Rectangle(100, 200, "red"))
## Large rectangle
match_rectangle(Rectangle(50, 60, "blue"))
## Rectangle: width=50, height=60, color=blue
match_rectangle(None)
## Not a Rectangle
