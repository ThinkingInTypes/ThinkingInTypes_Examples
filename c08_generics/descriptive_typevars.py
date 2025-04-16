# descriptive_typevars.py
from typing import TypeVar, Generic

KT = TypeVar("KT")  # Key type
VT = TypeVar("VT")  # Value type


class BiMap(Generic[KT, VT]): ...
