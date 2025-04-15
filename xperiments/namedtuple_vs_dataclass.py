from dataclasses import dataclass, fields, is_dataclass
from typing import NamedTuple


class NT(NamedTuple):  # Immutable
    name: str
    price: float


@dataclass(frozen=True)  # Also immutable
class FDC:
    name: str
    price: float


nt = NT("Plumbus", 1.29)
fdc = FDC("Plumbus", 1.29)

print(nt)
print(fdc)

# They are different types:
print(f"{nt == fdc = }")
print(f"{type(nt) = }")
print(f"{type(fdc) = }")

# Access by index
print(f"{nt[1] = }")
# Dataclasses does not support indexing

# NamedTuple introspection
print("\nNamedTuple methods:")
print(f"{nt._asdict() = }")

# Dataclass introspection
print("\nDataclass fields:")
if is_dataclass(FDC):
    for f in fields(FDC):
        print(f"{f.name}: {f.type}")

# Create new object by replacing a value:
nt2 = nt._replace(name="Desktop")
print(f"{nt2 = }")
print(f"{nt == nt2 = }")

# NamedTuple fields
print("\nNamedTuple _fields:")
print(f"{nt._fields = }")


# NamedTuple with default values
class NTWithDefaults(NamedTuple):
    name: str = "Unknown"
    price: float = 0.0


nt_defaults = NTWithDefaults()
print(f"{nt_defaults = }")
print(f"{NTWithDefaults._fields = }")
print(f"{NTWithDefaults._field_defaults = }")
