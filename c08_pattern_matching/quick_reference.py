# quick_reference.py
from typing import TypedDict, Literal, Any


def literal_example(value: int) -> None:
    match value:
        case 42:
            print("The Answer")
        case _:
            print("Not the Answer")


def capture_example(value: Any) -> None:
    match value:
        case x:
            print(f"Got: {x}")


def wildcard_example(value: Any) -> None:
    match value:
        case _:
            print("Don't care")


def sequence_example(value: Any) -> None:
    match value:
        case [x, y]:
            print(f"Sequence of length 2: x={x}, y={y}")
        case _:
            print("Not a 2-element sequence")


class Event(TypedDict):
    type: Literal["keypress"]
    key: str


def mapping_example(event: Any) -> None:
    match event:
        case {"type": "keypress", "key": k}:
            print(f"Key pressed: {k}")
        case _:
            print("Not a keypress event")


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def class_example(value: Any) -> None:
    match value:
        case Point(x=px, y=py):
            print(f"Point: x={px}, y={py}")
        case _:
            print("Not a Point")


def or_pattern_example(value: int) -> None:
    match value:
        case 0 | 1:
            print("Zero or one")
        case _:
            print("Something else")


def as_pattern_example(value: Any) -> None:
    match value:
        case [x, y] as pair:
            print(f"Pair: {pair}, elements: {x}, {y}")
        case _:
            print("Not a pair")


def guard_example(value: int) -> None:
    match value:
        case x if x > 10:
            print("Greater than 10")
        case _:
            print("10 or below")
