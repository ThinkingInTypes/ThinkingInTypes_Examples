# literal_patterns.py


def info(status: int) -> str:
    match status:
        case 200:
            return f"{status:03d}: OK"
        case 404:
            return f"{status:03d}: Not Found"
        case _:
            return f"{status:03d}: Unknown status"


print(info(200))
## 200: OK
print(info(404))
## 404: Not Found
print(info(500))
## 500: Unknown status
