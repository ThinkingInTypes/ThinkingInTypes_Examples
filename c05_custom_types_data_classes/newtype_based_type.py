# newtype_based_type.py
from typing import NewType

Stars = NewType("Stars", int)

GasGiants = NewType("GasGiants", Stars)
