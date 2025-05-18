# literal_1.py
from typing import Literal

ParamVal = Literal["MIN", "MAX", "DEF"]
print(ParamVal)
## typing.Literal['MIN', 'MAX', 'DEF']
print("MIN" in ParamVal)
## False
print("NOPE" in ParamVal)
## False

# Convert literal values to a set:
allowed_set = set(ParamVal.__args__)  # type: ignore
print(allowed_set)
## {'MIN', 'DEF', 'MAX'}
print("MIN" in allowed_set)
## True
print("NOPE" in allowed_set)
## False
