# example_16.py
from colors import Color


## It's green!


def handle_color(color: Color):
    match color:
        case Color.RED | Color.GREEN | Color.BLUE:
            ...  # handle known colors
        case _ as unknown:
            raise ValueError(f"Unknown color: {unknown}")
