# example_5.py
from example_4 import quacks
## Quack!
## I can quack, too!

try:
    quacks(42)
except AttributeError as e:
    print(f"Oops: {e = }")
## Oops: e = AttributeError("'int' object has no
## attribute 'quack'")
