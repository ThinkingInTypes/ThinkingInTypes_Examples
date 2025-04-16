# example_8.py
def rest_pattern(*values):
    match values:
        case [first, second, *rest]:
            print(
                f"{first = }, {second = }, {rest = }"
            )


rest_pattern(10, 20, 30, 40)
## first = 10, second = 20, rest = [30, 40]
rest_pattern("a", "b", "c", "d")
## first = 'a', second = 'b', rest = ['c', 'd']
