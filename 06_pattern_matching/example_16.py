# example_16.py
from example_2 import Color


def handle_color(color: Color):
    match color:
        case Color.RED | Color.GREEN | Color.BLUE:
            ...  # handle known colors
        case _ as unknown:
            raise ValueError(
                f"Unknown color: {unknown}"
            )
