# example_12.py
def f(x: int) -> int:
    return x * 2


print(f(5))  # Correct type
## 10
# Expected type 'int', got 'str' instead:
print(f("hi"))  # type: ignore
## hihi
# Strings can be "multiplied"
