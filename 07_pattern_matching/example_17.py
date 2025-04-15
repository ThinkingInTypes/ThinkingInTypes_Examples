# example_17.py
pair = (5, 5)
match pair:
    case (x, y) if x == y:
        print("The two values are equal.")
    case (x, y):
        print("The values are different.")
## The two values are equal.
