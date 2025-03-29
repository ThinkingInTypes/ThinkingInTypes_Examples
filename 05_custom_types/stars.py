# stars.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Stars:
    number: int
    def __post_init__(self) -> None:
        assert 1 <= self.number <= 10, f"{self}"

def f1(s: Stars) -> Stars:
    return Stars(s.number + 5)

def f2(s: Stars) -> Stars:
    return Stars(s.number * 5)

stars1 = Stars(4)
print(stars1)
print(f1(stars1))
print(f2(f1(stars1)))
stars2 = Stars(11)
print(f1(stars2))
