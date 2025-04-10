# example_12.py
def f(x: int) -> int:
    return x * 2

print(f(5))      # 10, type is correct
## 10
print(f("hi"))   # This will actually raise a TypeError at runtime, 
## hihi
                 # because Python tries to do "hi" * 2 (which surprisingly works for strings by repetition!)
