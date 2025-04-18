# look_inside.py


def attributes(d: object) -> str:
    return (
        ", ".join(
            [
                f"{k}: {v}"
                for k, v in vars(d).items()
                if not k.startswith("__")
            ]
        )
        or "Empty"
    )


def show(obj: object, obj_name: str) -> None:
    klass: type = obj.__class__
    print(f"[Class {klass.__name__}] {attributes(klass)}")
    print(f"[Object {obj_name}] {attributes(obj)}")
