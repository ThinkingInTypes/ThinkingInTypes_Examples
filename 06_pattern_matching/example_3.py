# example_3.py
command = "hello"
match command:
    case "quit":
        print("Quitting...")
    case other:
        print(f"Received unknown command: {other!r}")
