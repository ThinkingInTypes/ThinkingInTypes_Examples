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
## {'data': __main__.Measurements, 'return': <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
