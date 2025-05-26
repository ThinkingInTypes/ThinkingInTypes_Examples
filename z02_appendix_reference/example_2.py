# example_2.py
from typing import ClassVar

from icecream import ic


class Starship:
    # Annotated class variable:
    stats: ClassVar[str] = ""
    # Un-annotated class variable:
    damage: int = 10


starship = Starship()
# print(starship.stats)
# print(Starship.damage)
# print(starship.damage)
# print(f"{Starship.__dict__ =}")
ic(Starship.__dict__)
starship.damage = 20
ic(Starship.__dict__)
# print(Starship.damage)
# print(starship.damage)
# print(f"{Starship.__dict__ =}")
