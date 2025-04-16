# example_5.py
from typing import Final, Sequence

data1: Final = [
    1,
    2,
    3,
]  # `data1` won't be re-assigned, but list can mutate
data2: Final[Sequence[int]] = [
    1,
    2,
    3,
]  # `data2` treated as Sequence, so no mutation methods
