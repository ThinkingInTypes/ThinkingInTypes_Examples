# example_19.py


def narrow(obj):
    match obj:
        case list as lst if all(
            isinstance(x, int) for x in lst
        ):
            # Here, lst is a list and we asserted all elements are int.
            total: int = sum(lst)
