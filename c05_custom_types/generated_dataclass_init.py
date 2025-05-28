# generated_dataclass_init.py
from dataclasses import dataclass, fields


@dataclass
class Point:
    x: int = 1
    y: int = 2

    @classmethod
    def show_generated_init(cls) -> None:
        params = [
            f"{f.name}: "
            f"{getattr(f.type, '__name__', repr(f.type))} = "
            f"{repr(f.default)}"
            for f in fields(cls)
        ]
        print(f"def __init__(self, {', '.join(params)}):")
        for f in fields(cls):
            print(f"    self.{f.name} = {f.name}")


Point.show_generated_init()
## def __init__(self, x: int = 1, y: int = 2):
##     self.x = x
##     self.y = y
