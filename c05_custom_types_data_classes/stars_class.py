# stars_class.py
from typing import Optional
from book_utils import Catch


class Stars:
    def __init__(self, n_stars: int):
        self._number = n_stars  # Private by convention
        self.validate()

    def validate(self, s: Optional[int] = None):
        if s:
            assert 1 <= s <= 10, f"{self}: {s}"
        else:
            assert 1 <= self._number <= 10, f"{self}"

    # Prevent external modification:
    @property
    def number(self):
        return self._number

    def __str__(self) -> str:
        return f"Stars({self._number})"

    # Every member function must validate the private variable:
    def f1(self, n_stars: int) -> int:
        self.validate(n_stars)  # Precondition
        self._number = n_stars + 5
        self.validate()  # Postcondition
        return self._number

    def f2(self, n_stars: int) -> int:
        self.validate(n_stars)  # Precondition
        self._number = n_stars * 5
        self.validate()  # Postcondition
        return self._number


stars1 = Stars(4)
print(stars1)
## Stars(4)
print(stars1.f1(3))
## 8
with Catch():
    print(stars1.f2(stars1.f1(3)))
## Error: Stars(40)
with Catch():
    stars2 = Stars(11)
## Error: Stars(11)
stars3 = Stars(5)
print(stars3.f1(4))
## 9
with Catch():
    print(stars3.f2(22))
## Error: Stars(9): 22
# @property without setter prevents mutation:
with Catch():
    stars1.number = 99  # type: ignore
