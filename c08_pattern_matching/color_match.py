# color_match.py
from colors import Color

color = Color.GREEN
match color:
    case Color.RED:
        print("color is red!")
    case Color.GREEN:
        print("color is green!")
    case Color.BLUE:
        print("color is blue!")
## color is green!
