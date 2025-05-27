# dataclass_with_init.py
from dataclasses import dataclass


@dataclass
class D:
    x: int = 1
    y: int = 2

    def __init__(self):
        pass


d = D()
print(f"{D.x = }, {D.y = }, {d.__dict__ = }")
d.x = 99
print(f"{D.x = }, {D.y = }, {d.__dict__ = }")
d.y = 111
print(f"{D.x = }, {D.y = }, {d.__dict__ = }")
