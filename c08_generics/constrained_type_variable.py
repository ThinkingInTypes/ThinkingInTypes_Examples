# constrained_type_variable.py

def add[Number:(int, float)](a: Number, b: Number) -> Number:
    return a + b


add(5, 10)  # valid, both int
add(3.5, 2.5)  # valid, both float
# ERROR: cannot mix types:
add(5, 2.5)  # type: ignore
# ERROR: str not allowed for Number:
add("A", "Z")  # type: ignore
