# example_12.py
user_input = "y"
match user_input.lower:
    case "yes" | "y" | "yeah":
        print("User said yes")
    case "no" | "n" | "nope":
        print("User said no")
    case _:
        print("Unrecognized response")
## Unrecognized response
