# example_13.py
def type_narrowing(data: int | float | str):
    match data:
        case int(x) | float(x):
            ...
            # handle as numeric (x will be int or float here)
        case str(s):
            ...
            # handle as string
