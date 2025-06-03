# enum_str_auto.py
from enum import StrEnum, auto


class Pets(StrEnum):
    DOG = auto()
    CAT = auto()
    HAMSTER = auto()


for p in Pets:
    print(f"{p.name = }: {p.value = }")
## p.name = 'DOG': p.value = 'dog'
## p.name = 'CAT': p.value = 'cat'
## p.name = 'HAMSTER': p.value = 'hamster'
