# example_4.py
def wildcard(status):
    match status:
        case 200:
            message = "OK"
        case 404:
            message = "Not Found"
        case _:
            message = "Unknown"  # `_` matches anything not matched above
