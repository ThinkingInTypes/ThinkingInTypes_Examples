# example_7.py
def add(a: int, b: int) -> int:
    return a + b


result = add(10, 5)
print(result)  # 15

result = add(
    10, "5"
)  # This will run, but likely cause a TypeError at runtime
