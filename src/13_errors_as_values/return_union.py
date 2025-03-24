# return_union.py
# Type union aka Sum Type
# Success vs error is not clear


def func_a(i: int) -> int | str:  # Sum type
    if i == 1:
        return f"func_a({i})"
    return i


print(outputs := [(i, func_a(i)) for i in range(5)])

for i, r in outputs:
    match r:
        case int(answer):
            print(f"{i}: {answer = }")
        case str(error):
            print(f"{i}: {error = }")
