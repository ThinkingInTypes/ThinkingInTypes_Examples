# example_15.py
data = {"coords": [7, 3]}
match data:
    case {"coords": [x, y] as point}:
        print(f"Point {point} has x={x}, y={y}")
