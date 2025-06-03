# traffic_light.py
from enum import Enum, auto


class TrafficLight(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()


def action(light: TrafficLight) -> str:
    match light:
        case TrafficLight.RED:
            return "Stop now"
        case TrafficLight.YELLOW:
            return "Proceed with caution"
        case TrafficLight.GREEN:
            return "Go"
        case _:  # Should not need this (exhaustivity)
            return "Unknown state"


for light in TrafficLight:
    print(f"{light.name}: {action(light)}")
## RED: Stop now
## YELLOW: Proceed with caution
## GREEN: Go
