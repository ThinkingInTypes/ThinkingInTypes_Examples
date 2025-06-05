# wildcard_final_case.py


def wildcard(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:  # Matches anything not matched above
            return "Unknown"
