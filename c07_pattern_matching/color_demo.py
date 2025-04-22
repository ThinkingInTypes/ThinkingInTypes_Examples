# color_demo.py
from colors import Color

color = Color.GREEN
match color:
    case Color.RED:
        print("It's red!")
    case Color.GREEN:
        print("It's green!")
    case Color.BLUE:
        print("It's blue!")
## It's green!
