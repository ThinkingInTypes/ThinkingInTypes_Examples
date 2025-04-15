# wildcard_ignore_elements.py
from typing import Any

def wildcard_ignore(point: tuple[float, Any, Any]) -> None:
    match point:
        case (x, _, _):
            print(f"x-coordinate is {x}")
