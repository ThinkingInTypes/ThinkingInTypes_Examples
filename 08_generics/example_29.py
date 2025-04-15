# example_29.py
from typing import TypeVar

T = TypeVar('T')

def set_value(x: T) -> None:
    global global_var
    global_var = x
