# typevars.py
from typing import TypeVar

T = TypeVar("T")  # Define a TypeVar named T


def identity(value: T) -> T:
    return value


print(identity(42))
## 42
print(identity("Hello"))
## Hello
