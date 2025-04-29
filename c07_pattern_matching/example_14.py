# example_14.py
pair = [4, 5]
match pair:
    case [first, second] as full_pair:
        print(f"First element: {first}, second: {second}, pair: {full_pair}")
## First element: 4, second: 5, pair: [4, 5]
