# like_default_values.py


class A:
    x: int = 100


a = A()
print(f"{a.x = }")
a.x = -1
print(f"{a.x = }")
a2 = A()
print(f"{a2.x = }")
