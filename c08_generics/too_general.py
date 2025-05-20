# too_general.py

def sort_items[T](items: list[T]) -> list[T]:
    # PyRight issue:
    return sorted(items)  # type: ignore
