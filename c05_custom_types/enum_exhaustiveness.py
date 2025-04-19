# enum_exhaustiveness.py
from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


# Did you intentionally leave out Color.BLUE?
def paint1(color: Color) -> str:
    if color == Color.RED:
        return "You chose red"
    elif color == Color.GREEN:
        return "You chose green"
    else:
        return "Something else"


print(paint1(Color.BLUE))


# Exhaustiveness checking:
def paint2(color: Color) -> str:
    match color:
        case Color.RED:
            return "You chose red"
        case Color.GREEN:
            return "You chose green"
        case Color.BLUE:
            return "You chose blue"
