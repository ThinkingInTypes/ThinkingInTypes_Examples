# simple_type_aliasing.py
from typing import get_type_hints, NewType

type Number = int | float | str
# Runtime-safe distinct type for measurement lists
Measurements = NewType("Measurements", list[Number])


def process_measurements(data: Measurements) -> None:
    print(get_type_hints(process_measurements))
    for n in data:
        print(f"{n = }, {type(n) = }")


process_measurements(Measurements([11, 3.14, "1.618"]))
