# display_attributes.py


def display_attributes(obj: any) -> None:
    """
    Display class variables and instance variables of the given object.

    - Class variables are attributes found in the class dict but not in the instance dict.
    - Instance variables are attributes found in the instance dict.
    """
    cls = obj.__class__
    cls_vars = {
        k: v
        for k, v in cls.__dict__.items()
        if not k.startswith("__") and k not in obj.__dict__
    }
    print(f"{'Class Variables':=^25}")
    for k, v in cls_vars.items():
        print(f"{k}: {v}")

    print(f"\n{'Instance Variables':=^25}")
    for k, v in obj.__dict__.items():
        print(f"{k}: {v}")


if __name__ == "__main__":

    class A:
        x: int = 100

    a = A()
    display_attributes(a)
    a.x = 200
    display_attributes(a)
