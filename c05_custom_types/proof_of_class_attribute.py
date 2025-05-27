# proof_of_class_attribute.py
from a_with_x import A

a = A()
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
## A.x = 1, a.__dict__ = {}, a.x = 1
a.x = 2
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
## A.x = 1, a.__dict__ = {'x': 2}, a.x = 2
