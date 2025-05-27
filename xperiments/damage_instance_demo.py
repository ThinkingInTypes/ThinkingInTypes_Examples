# damage_instance_demo.py

from typing import ClassVar


class Starship:
    stats: ClassVar[dict[str, int]] = {}  # class variable
    damage: int = 10  # instance variable, not a class variable


def main() -> None:
    print("Accessing via class:")
    print(
        f"Starship.stats: {Starship.stats}"
    )  # This works: ClassVar
    print(
        f"Starship.damage: {Starship.damage}"
    )  # This works at runtime (but not a ClassVar)

    s1 = Starship()
    s2 = Starship()

    print("\nInitial instance values:")
    print(f"s1.damage: {s1.damage}")
    print(f"s2.damage: {s2.damage}")

    print("\nModifying s1.damage to 99...")
    s1.damage = 99

    print("\nAfter modification:")
    print(f"s1.damage: {s1.damage}")  # Changed
    print(f"s2.damage: {s2.damage}")  # Unchanged
    print(f"Starship.damage: {Starship.damage}")  # Still 10

    print("\nChecking instance __dict__:")
    print(f"s1.__dict__: {s1.__dict__}")
    print(f"s2.__dict__: {s2.__dict__}")
    print(
        f"Starship.__dict__['damage']: {Starship.__dict__['damage']}"
    )

    print("\nConclusion:")
    print(
        "- 'damage' exists in Starship.__dict__ because it was defined at the class level."
    )
    print(
        "- But it's not a ClassVar, so when accessed via an instance, it's copied into instance.__dict__."
    )
    print("- Each instance has its own copy of 'damage'.")


if __name__ == "__main__":
    main()
