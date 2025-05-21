# new_type.py
from typing import NewType, get_type_hints

type Number = int | float | str  # Static union alias

# Runtime-safe distinct type:
Measurements = NewType("Measurements", list[Number])


def process(data: Measurements) -> None:
    print(get_type_hints(process))
    for n in data:
        print(f"{n = }, {type(n) = }")


process(Measurements([11, 3.14, "1.618"]))
