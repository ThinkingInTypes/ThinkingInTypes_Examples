# double_star_wildcard.py
user_info = {
    "name": "Alice",
    "age": 30,
    "country": "US",
}
match user_info:
    case {"name": name, **rest}:
        print(f"Name is {name}, other info: {rest}")
