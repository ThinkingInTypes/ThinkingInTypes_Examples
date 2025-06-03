# example_16.py
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


def handle_color(color: Color):
    match color:
        case Color.RED | Color.GREEN | Color.BLUE:
            print(f"Color is {color.name.lower()}")
        # Exhaustiveness produces: "code is unreachable":
        # // Need a different example
        # case _ as unknown:
        #     raise ValueError(f"Unknown color: {unknown}")


for color in Color:
    handle_color(color)
## Color is red
## Color is green
## Color is blue
