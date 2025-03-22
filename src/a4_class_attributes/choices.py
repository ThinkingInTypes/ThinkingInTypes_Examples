# choices.py
from look_inside import show
from dataclasses import dataclass


class A:
    def __init__(self, x: int = 100, y: int = 200, z: int = 300):
        self.x = x
        self.y = y
        self.z = z


# OR:


@dataclass
class AA:
    x: int = 100
    y: int = 200
    z: int = 300


a = A()
show(a, "a")
a.x = -1
a.y = -2
a.z = -3
show(a, "a")

aa = AA()
print(aa)
show(aa, "aa")
aa.x = -1
aa.y = -2
aa.z = -3
show(aa, "aa")
aa2 = AA(-4, -5, -6)
show(aa2, "aa2")

# Even if we modify the class attributes, the
# constructor default arguments stay the same:
AA.x = 42
AA.y = 74
AA.z = 22
aa3 = AA()
show(aa3, "aa3")
