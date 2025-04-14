# new_type.py
from typing import NewType, get_type_hints

Number = NewType("Number", int | float | str)
Measurements = NewType("Measurements", list[Number])


def process_measurements(data: Measurements) -> None:
    print(get_type_hints(process_measurements))
    for n in data:
        print(f"{n = }, {type(n) = }")


process_measurements(
    Measurements(
        [Number(11), Number(3.14), Number("1.618")]
    )
)
## {'data': __main__.Measurements, 'return':
## <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
process_measurements(Measurements([11, 3.14, "1.618"]))
## {'data': __main__.Measurements, 'return':
## <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
# Not allowed:
# process_measurements([11, 3.14, "1.618"])
