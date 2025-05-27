# dataclass_attribute.py
from dataclasses import dataclass


@dataclass
class A:
    x: int = 1


a = A()
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
## A.x = 1, a.__dict__ = {'x': 1}, a.x = 1
a.x = 2
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
## A.x = 1, a.__dict__ = {'x': 2}, a.x = 2
