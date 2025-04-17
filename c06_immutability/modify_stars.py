# modify_stars.py
from stars import Stars


## Stars(number=4)
## Stars(number=9)
## Error: Stars(number=45)
## Error: Stars(number=11)
## Error: Stars(number=11)


def increase_stars(rating: Stars, increment: int) -> Stars:
    return Stars(rating.number + increment)
