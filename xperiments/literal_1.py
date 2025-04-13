# literal_to_set.py
from typing import Literal

ParamVal = Literal["MIN", "MAX", "DEF"]
print(ParamVal)
print("MIN" in ParamVal)
print("NOPE" in ParamVal)

# Convert literal values to a set:
allowed_set = set(ParamVal.__args__)  # type: ignore
print(allowed_set)
print("MIN" in allowed_set)
print("NOPE" in allowed_set)
