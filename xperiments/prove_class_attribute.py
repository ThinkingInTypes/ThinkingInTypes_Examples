# prove_class_attribute.py
class A:
    x = 1


a = A()
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
a.x = 2
print(f"{A.x = }, {a.__dict__ = }, {a.x = }")
