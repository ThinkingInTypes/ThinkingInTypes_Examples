# nested_patterns.py


def nested_pattern(*values: int) -> None:
    match values:
        case [first, second, *rest]:
            # Here the type checker infers:
            #--first: int
            #--second: int
            #--rest: list[int]
            print(f"{first = }, {second = }, {rest = }")
        case [(x, y), *rest]:
            print(f"({x=}, {y=}), *{rest}")


nested_pattern(10, 20, 30, 40)
## first = 10, second = 20, rest = [30, 40]
nested_pattern((50, 60), 70, 80)
## first = (50, 60), second = 70, rest = [80]
