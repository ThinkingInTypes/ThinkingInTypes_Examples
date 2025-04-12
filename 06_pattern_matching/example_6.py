# example_6.py
from typing import NamedTuple


class Player(NamedTuple):
    name: str
    score: int


def player_score(player: Player):
    match player:
        case Player(name=_, score=s):
            print(f"Player has score {s}")
