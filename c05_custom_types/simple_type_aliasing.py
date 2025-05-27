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
## {'data': __main__.Measurements, 'return':
## <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
