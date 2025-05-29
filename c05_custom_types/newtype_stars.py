# newtype_stars.py
from typing import NewType

Stars = NewType("Stars", int)


def f1(stars: Stars) -> Stars:
    assert 1 <= stars <= 10, f"f1: {stars}"
    return Stars(stars + 5)


def f2(stars: Stars) -> Stars:
    assert 1 <= stars <= 10, f"f2: {stars}"
    return Stars(stars * 5)
