# subject_annotations.py


def subject_annotation(*values: int) -> None:
    match values:
        case [first, second, *rest]:
            # Here the type checker infers:
            # --first: int
            # --second: int
            # --rest: list[int]
            print(f"{first = }, {second = }, {rest = }")


subject_annotation(10, 20, 30, 40)
## first = 10, second = 20, rest = [30, 40]
subject_annotation(10, 20, 30, "40")  # type: ignore
## first = 10, second = 20, rest = [30, '40']
subject_annotation("a", "b", "c", "d")  # type: ignore
## first = 'a', second = 'b', rest = ['c', 'd']
