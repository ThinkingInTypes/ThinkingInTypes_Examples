# example_3.py
from typing import TypedDict


class Command(TypedDict):
    action: str
    payload: dict


def process_command(command: TypedDict) -> None:
    match command:
        case {"action": "create", "item": item}:
            print(f"Creating {item}")
        case {"action": "delete", "id": int() as item_id}:
            print(f"Deleting item {item_id}")
        case _:
            print("Unknown command")
