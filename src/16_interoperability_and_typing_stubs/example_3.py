# example_3.py
# custom_module.pyi
class User:
    id: int
    name: str


def fetch_user(user_id: int) -> User: ...
