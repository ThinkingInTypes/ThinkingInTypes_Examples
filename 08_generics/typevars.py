# typevars.py
from typing import TypeVar

T = TypeVar("T")  # Define a TypeVar named T


def echo(value: T) -> T:
    return value


print(echo(42))
## 42
print(echo("Hello"))
## Hello
