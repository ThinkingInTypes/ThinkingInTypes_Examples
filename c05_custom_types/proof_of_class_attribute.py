# proof_of_class_attribute.py
from class_and_instance import show_dicts


class A:
    x: int = 1
    y: int = 2


a = A()
show_dicts(a, "a", "Initialization")
a.x = 99
show_dicts(a, "a", "a.x = 99")
a.y = 111
show_dicts(a, "a", "a.y = 111")
