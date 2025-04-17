# accidental_genericity.py
from typing import TypeVar

T = TypeVar("T")

global_var = None  # Mypy requires to avoid NameError


# warning: TypeVar "T" appears only once
# in generic function signature:
def set_value(x: T) -> None:  # type: ignore
    global global_var
    global_var = x
