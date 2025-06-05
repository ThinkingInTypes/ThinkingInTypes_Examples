# before_and_after.py

# Before pattern matching
def process_data_before(data):
    if isinstance(data, dict):
        if "type" in data:
            if data["type"] == "user":
                return f"User: {data.get('name', 'Unknown')}"
            elif data["type"] == "product":
                return (
                    f"Product: {data.get('title', 'Untitled')}"
                )
    elif isinstance(data, list) and len(data) == 2:
        return f"Coordinates: ({data[0]}, {data[1]})"
    return "Unknown data"


# After pattern matching
def process_data_after(data):
    match data:
        case {"type": "user", "name": name}:
            return f"User: {name}"
        case {"type": "product", "title": title}:
            return f"Product: {title}"
        case [x, y]:
            return f"Coordinates: ({x}, {y})"
        case _:
            return "Unknown data"
