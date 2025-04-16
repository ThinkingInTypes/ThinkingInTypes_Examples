# generic_zip.py
from typing import Callable, TypeVarTuple, reveal_type

Ts = TypeVarTuple("Ts")


def zip_variadic(*args: *Ts) -> tuple[*Ts]:
    return args


reveal_type(zip_variadic(1, "a", 3.14))
# tuple[int, str, float]
