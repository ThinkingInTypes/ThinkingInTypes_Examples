from dataclasses import dataclass

@dataclass(init=False)
class Record[*Fields]:
    fields: tuple[*Fields]

    def __init__(self, *fields: *Fields) -> None:
        self.fields = fields

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(fields={self.fields})"

    def to_tuple(self) -> tuple[*Fields]:
        return self.fields


r1 = Record(1, "Alice", 3.14)
r2 = Record(True, None)

print(r1.to_tuple())
# (1, 'Alice', 3.14)
print(r2.to_tuple())
# (True, None)
