# mutable_defaults.py
# Pitfalls in NamedTuple vs safe handling in dataclass
from dataclasses import dataclass, field
from typing import NamedTuple


class NTBag(NamedTuple):
    # Don't do this -- shared across all instances:
    items: list[str] = []


@dataclass(frozen=True)
class DCBag:
    # Default factory makes a new list for each instance:
    items: list[str] = field(default_factory=list)


nt1 = NTBag()
nt1.items.append("apple")
nt2 = NTBag()

print(f"{nt1.items = }")
# Also has 'apple' due to shared list:
print(f"{nt2.items = }")

dc1 = DCBag()
dc2 = DCBag()
# Can't mutate frozen dataclasses directly, create new one:
dc1_updated = DCBag(items=dc1.items + ["banana"])

print(f"{dc1_updated.items = }")
print(f"dc2.items = {dc2.items}")  # Still empty
