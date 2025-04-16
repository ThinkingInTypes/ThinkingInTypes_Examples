# literal_to_set.py
from typing import Literal

ParamVal = Literal["DEF", "MIN", "MAX"]
print(ParamVal)
## typing.Literal['DEF', 'MIN', 'MAX']
print("MIN" in ParamVal)  # type: ignore
## False
print("NOPE" in ParamVal)  # type: ignore
## False

# Convert literal values to a set:
allowed_set = set(ParamVal.__args__)  # type: ignore
print(allowed_set)
## {'MAX', 'DEF', 'MIN'}
print("MIN" in allowed_set)
## True
print("NOPE" in allowed_set)
## False
