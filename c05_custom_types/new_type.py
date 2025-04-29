# new_type.py
from typing import NewType, get_type_hints

# Correct, but not all type checkers have caught up:
Number = NewType("Number", int | float | str)  # type: ignore
Measurements = NewType("Measurements", list[Number])


def process(data: Measurements) -> None:
    print(get_type_hints(process))
    for n in data:
        print(f"{n = }, {type(n) = }")


process(Measurements([Number(11), Number(3.14), Number("1.618")]))
## {'data': __main__.Measurements, 'return':
## <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
process(Measurements([11, 3.14, "1.618"]))  # type: ignore
## {'data': __main__.Measurements, 'return':
## <class 'NoneType'>}
## n = 11, type(n) = <class 'int'>
## n = 3.14, type(n) = <class 'float'>
## n = '1.618', type(n) = <class 'str'>
# Not allowed:
# process_measurements([11, 3.14, "1.618"])
