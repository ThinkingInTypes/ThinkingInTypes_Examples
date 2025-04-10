# example_5.py
from example_4 import quacks

try:
    quacks(42)
except AttributeError as e:
    print(f"Oops: {e = }")
