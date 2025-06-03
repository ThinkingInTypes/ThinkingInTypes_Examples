# example_17.py
pair = (5, 5)
match pair:
    case (x, y) if x == y:
        print("Values are equal.")
    case (x, y):
        print("Values are different.")
## Values are equal.
