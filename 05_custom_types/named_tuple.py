# named_tuple.py
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


coords = Coordinates(51.5074, -0.1278)
print(coords)
print(coords.latitude)
# coords.latitude = 123.4567 # Runtime error
