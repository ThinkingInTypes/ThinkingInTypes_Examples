# colors.py
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


color = Color.GREEN
match color:
    case Color.RED:
        print("It's red!")
    case Color.GREEN:
        print("It's green!")
    case Color.BLUE:
        print("It's blue!")
## It's green!
