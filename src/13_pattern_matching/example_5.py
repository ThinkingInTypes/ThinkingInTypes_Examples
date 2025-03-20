# example_5.py
def process_response(response: dict) -> str:
    match response:
        case {"status": "success", "data": data}:
            return f"Success: {data}"
        case {"status": "error", "message": error_msg}:
            return f"Error: {error}"
        case _:
            return "Unknown response format"
