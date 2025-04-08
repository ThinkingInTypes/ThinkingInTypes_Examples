# example_6.py
def parse_coordinates(coords: tuple) -> str:
    match coords := coords:
        case (float(lat), float(lon)):
            return f"Latitude: {lat}, Longitude: {lon}"
        case _:
            return "Invalid coordinates"
