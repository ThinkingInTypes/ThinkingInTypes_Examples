# mapping_patterns.py
from typing import Literal, TypedDict


class KeyPressEvent(TypedDict):
    type: Literal["keypress"]
    key: str


class MouseMoveEvent(TypedDict):
    type: Literal["mousemove"]
    x: int
    y: int


Event = KeyPressEvent | MouseMoveEvent


def event_info(event: Event) -> None:
    match event:
        case {"type": "keypress", "key": k}:
            print(f"Key pressed: {k}")
        case {"type": "mousemove", "x": x, "y": y}:
            print(f"Mouse moved to ({x}, {y})")
        case _:
            print("Unknown event")


e1: KeyPressEvent = {"type": "keypress", "key": "Enter"}
e2: MouseMoveEvent = {"type": "mousemove", "x": 47, "y": 42}

event_info(e1)
## Key pressed: Enter
event_info(e2)
## Mouse moved to (47, 42)
