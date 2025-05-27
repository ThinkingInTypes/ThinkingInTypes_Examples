# a_with_x.py
class A:
    x: int = 1  # Does it create an instance attribute?


a = A()
print(f"{a.x = }")
## a.x = 1
