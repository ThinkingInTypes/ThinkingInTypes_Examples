# example_17.py
def calculate_area(radius: int) -> float:
    return 3.14 * radius**2


calculate_area(3.5)  # R: Flagged by static type checker
