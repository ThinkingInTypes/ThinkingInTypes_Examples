# class_attributes.py
from look_inside import show


class A:
    x: int = 100


class B:
    x: int = 100

    def __init__(self, x_init: int):
        # Shadows the class attribute name:
        self.x = x_init


a = A()
show(a, "a")
a.x = 1
show(a, "a")
b = B(-99)
show(b, "b")
