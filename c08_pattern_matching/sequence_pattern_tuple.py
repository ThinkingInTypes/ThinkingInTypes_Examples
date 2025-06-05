# sequence_pattern_tuple.py


def where(point: object) -> str:
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On the Y-axis at y={y}"
        case (x, 0):
            return f"On the X-axis at x={x}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return f"Unknown {point = }"


for p in [(0, 0), (0, 1), (1, 0), (1, 1), tuple()]:
    print(where(p))
## Origin
## On the Y-axis at y=1
## On the X-axis at x=1
## Point at (1, 1)
## Unknown point = ()
