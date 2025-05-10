# example_6.py
def f(x: int) -> str:
    return x  # type: ignore      # This mismatches return type
    # pyre-ignore-all-errors[7]  # ignore "incompatible return type" for file
