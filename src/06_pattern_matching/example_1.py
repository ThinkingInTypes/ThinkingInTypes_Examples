# example_1.py
def handle_command(command: str) -> str:
    match command:
        case "start":
            return "Starting"
        case "stop":
            return "Stopping"
        case _:
            return "Unknown command"
