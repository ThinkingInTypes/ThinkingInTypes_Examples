# newtype_subtype.py
from typing import NewType

Stars = NewType("Stars", int)

# Fails type check and at runtime:
# class GasGiants(Stars): pass
