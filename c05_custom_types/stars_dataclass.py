# stars_dataclass.py
from dataclasses import dataclass

from book_utils import Catch


@dataclass
class Stars:
    number: int

    def __post_init__(self) -> None:
        assert 1 <= self.number <= 10, f"{self}"


def f1(stars: Stars) -> Stars:
    return Stars(stars.number + 5)


def f2(stars: Stars) -> Stars:
    return Stars(stars.number * 5)


stars1 = Stars(6)
print(stars1)
## Stars(number=6)
with Catch():
    print(f1(stars1))
## Error: Stars(number=11)
with Catch():
    print(f2(stars1))
## Error: Stars(number=30)
with Catch():
    print(f1(Stars(22)))
## Error: Stars(number=22)
with Catch():
    print(f2(Stars(99)))
## Error: Stars(number=99)
