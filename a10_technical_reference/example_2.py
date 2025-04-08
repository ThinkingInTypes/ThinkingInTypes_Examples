# example_2.py
from typing import ClassVar


class Starship:
    stats: ClassVar[dict[str, int]] = {}   # class variable  
    damage: int = 10                       # instance variable
