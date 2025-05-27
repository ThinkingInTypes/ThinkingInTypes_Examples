# a_with_x.py
class A:
    # Does this create instance attributes?
    x: int = 1
    y: int = 2


a = A()
print(f"{a.x = }, {a.y = }")
## a.x = 1
