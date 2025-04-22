# example_5.py
from duck_typing import quacks

try:
    quacks(42)
except AttributeError as e:
    print(f"Oops: {e = }")
## Oops: e = AttributeError("'int' object has no
## attribute 'quack'")
