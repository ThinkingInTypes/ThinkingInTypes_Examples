# example_9.py
event = {"type": "keypress", "key": "Enter"}
match event:
    case {"type": "keypress", "key": k}:
        print(f"Key pressed: {k}")
    case {"type": "mousemove", "x": x, "y": y}:
        print(f"Mouse moved to ({x}, {y})")
    case _:
        print("Unknown event")
## Key pressed: Enter
