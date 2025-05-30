# modify_stars.py
from stars import Stars


def increase_stars(rating: Stars, increment: int) -> Stars:
    return Stars(rating.number + increment)
