# example_5.py
def wildcard_ignore(point):
    match point:
        case (x, _, _):
            print(f"x-coordinate is {x}")
