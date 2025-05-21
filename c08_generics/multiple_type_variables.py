# multiple_type_variables.py


def pairify[A, B](x: A, y: B) -> tuple[A, B]:
    return x, y


result = pairify("Alice", 5)  # tuple[str, int]
