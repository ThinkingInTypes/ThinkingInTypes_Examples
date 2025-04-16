# heterogenous_record.py
from typing import TypeVarTuple, Generic, Unpack

Fields = TypeVarTuple("Fields")


class Record(Generic[*Fields]):
    def __init__(self, *fields: *Fields):
        self.fields = fields

    def __repr__(self) -> str:
        return f"Record(fields={self.fields})"

    def to_tuple(self) -> tuple[*Fields]:
        return self.fields


r1 = Record(1, "Alice", 3.14)  # Record[int, str, float]
r2 = Record(True, None)  # Record[bool, NoneType]

print(r1.to_tuple())
print(r2.to_tuple())
