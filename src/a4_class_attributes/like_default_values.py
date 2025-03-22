# like_default_values.py


class A:
    x: int = 100


a = A()
print(f"{a.x = }")
## a.x = 100
# a.x = 100
a.x = -1
print(f"{a.x = }")
## a.x = -1
# a.x = -1
a2 = A()
print(f"{a2.x = }")
## a2.x = 100
# a2.x = 100
