# example_12.py
def f(x: int) -> int:
    return x * 2


print(f(5))  # Correct type
## 10
print(f("hi"))  # Does NOT cause a TypeError
## hihi
# Strings can be "multiplied"
