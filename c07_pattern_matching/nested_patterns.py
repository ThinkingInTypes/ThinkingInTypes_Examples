# nested_patterns.py
from typing import cast


def nested_pattern(*values: int) -> None:
    match values:
        case [first, second, *rest]:
            # Here the type checker infers:
            # --first: int
            # --second: int
            # --rest: list[int]
            print(
                f"{first = }, {second = }, {rest = }"
            )

        case [(x, y), *rest]:
            # Known pattern matching limitation in mypy:
            x, y = cast(tuple[int, int], rest)
            print(f"({x=}, {y=}), *{rest}")


nested_pattern(10, 20, 30, 40)
## first = 10, second = 20, rest = [30, 40]
# Type checkers haven't caught up:
nested_pattern((50, 60), 70, 80)  # type: ignore
## first = (50, 60), second = 70, rest = [80]
