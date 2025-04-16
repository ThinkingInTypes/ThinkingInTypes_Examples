# example_3.py
from typing import Optional


# Error: Incompatible return value type (got "None", expected "int")
def find_index(
        item: str, items: list[str]
) -> Optional[int]:
    try:
        return items.index(item)
    except ValueError:
        return None
