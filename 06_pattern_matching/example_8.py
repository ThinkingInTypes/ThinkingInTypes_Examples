# example_8.py

match values:
    case [first, second, *rest]:
        print(
            f"First={first}, second={second}, rest={rest}"
        )
