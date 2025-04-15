# example_1.py
status = 404
match status:
    case 200:
        result = "OK"
    case 404:
        result = "Not Found"
    case _:
        result = "Unknown status"
