# wildcard_final_case.py
def wildcard(status) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"  # `_` matches anything not matched above
