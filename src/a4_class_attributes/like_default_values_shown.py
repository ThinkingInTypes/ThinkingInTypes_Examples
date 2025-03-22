# like_default_values_shown.py
from look_inside import show


class A:
    x: int = 100


a = A()
show(a, "a")
print(f"{a.x = }")
a.x = -1
show(a, "a")
print(f"{a.x = }")
a2 = A()
show(a2, "a2")
print(f"{a2.x = }")
