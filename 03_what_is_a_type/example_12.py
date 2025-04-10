# example_12.py
def f(x: int) -> int:
    return x * 2


print(f(5))  # 10, type is correct
print(
    f("hi")
)  # This will actually raise a TypeError at runtime,
# because Python tries to do "hi" * 2 (which surprisingly works for strings by repetition!)
