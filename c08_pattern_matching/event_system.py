# event_system.py
from typing import TypedDict, Literal


class KeyPress(TypedDict):
    type: Literal["key_press"]
    key: str


class MouseMove(TypedDict):
    type: Literal["mouse_move"]
    x: int
    y: int


mouseButton = Literal["left", "right", "middle"]


class MouseClick(TypedDict):
    type: Literal["mouse_click"]
    x: int
    y: int
    button: mouseButton


class WindowResize(TypedDict):
    type: Literal["window_resize"]
    width: int
    height: int


Event = KeyPress | MouseMove | MouseClick | WindowResize


class EVT:
    @staticmethod
    def key_press(key: str) -> KeyPress:
        return {"type": "key_press", "key": key}

    @staticmethod
    def mouse_move(x: int, y: int) -> MouseMove:
        return {"type": "mouse_move", "x": x, "y": y}

    @staticmethod
    def mouse_click(
        x: int, y: int, button: mouseButton
    ) -> MouseClick:
        return {
            "type": "mouse_click",
            "x": x,
            "y": y,
            "button": button,
        }

    @staticmethod
    def window_resize(width: int, height: int) -> WindowResize:
        return {
            "type": "window_resize",
            "width": width,
            "height": height,
        }


def handle_event(event: Event) -> None:
    match event:
        case {"type": "key_press", "key": key}:
            print(f"Key press: {key}")
        case {"type": "mouse_move", "x": x, "y": y}:
            print(f"Mouse move to ({x}, {y})")
        case {
            "type": "mouse_click",
            "x": x,
            "y": y,
            "button": button,
        }:
            print(f"Mouse click: ({x}, {y}) button: {button}")
        case {"type": "window_resize", "width": w, "height": h}:
            print(f"Window resize to {w} x {h}")
        case _:
            print(f"Unknown event {event}")


for event in [
    EVT.key_press("A"),
    EVT.mouse_move(100, 200),
    EVT.mouse_click(10, 15, "left"),
    EVT.window_resize(800, 600),
]:
    handle_event(event)
## Key press: A
## Mouse move to (100, 200)
## Mouse click: (10, 15) button: left
## Window resize to 800 x 600
