# example_5.py
try:
    quacks(42)
except AttributeError as e:
    print("Oops:", e)
