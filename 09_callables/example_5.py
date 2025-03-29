# example_5.py
from typing import overload, Union


@overload
def double(value: int) -> int: ...


@overload
def double(value: str) -> str: ...


def double(value: Union[int, str]) -> Union[int, str]:
    if isinstance(value, int):
        return value * 2
    return value + value


print(double(4))  # Output: 8
## 8
print(double("Hi"))  # Output: HiHi
## HiHi
