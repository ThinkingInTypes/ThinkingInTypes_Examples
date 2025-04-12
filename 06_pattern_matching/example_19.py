# example_19.py


def narrow(obj):
    match obj:
        case list() as lst if all(
            isinstance(x, int) for x in lst
        ):
            # here, lst is a list and we asserted all elements are int
            total: int = sum(
                lst
            )  # type checker can assume lst is list[int]
