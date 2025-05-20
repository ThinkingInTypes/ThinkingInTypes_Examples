# heterogeneous_record.py
from dataclasses import dataclass


@dataclass
class Record[*Fields]:
    fields: tuple[*Fields]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(fields={self.fields})"


print(Record((1, "Alice", 3.14)))
## Record(fields=(1, 'Alice', 3.14))
print(Record((True, None)))
## Record(fields=(True, None))
