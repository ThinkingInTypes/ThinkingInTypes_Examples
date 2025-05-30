# return_union.py
# Type union aka Sum Type
# Success vs error is not clear


def fa(i: int) -> int | str:  # Sum type
    if i == 1:
        return f"fa({i})"
    return i


print(outputs := [(i, fa(i)) for i in range(5)])
## [(0, 0), (1, 'fa(1)'), (2, 2), (3, 3), (4, 4)]

for i, r in outputs:
    match r:
        case int(answer):
            print(f"{i}: {answer = }")
        case str(error):
            print(f"{i}: {error = }")
## 0: answer = 0
## 1: error = 'fa(1)'
## 2: answer = 2
## 3: answer = 3
## 4: answer = 4
