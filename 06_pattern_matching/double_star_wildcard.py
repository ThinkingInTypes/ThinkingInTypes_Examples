# double_star_wildcard.py
user_info = {
    "name": "Alice",
    "age": 30,
    "country": "US",
}

match user_info:
    case {"name": name, **rest}:
        print(f"Name: {name}, info: {rest}")
## Name is Alice, other info: {'age': 30,
## 'country': 'US'}
