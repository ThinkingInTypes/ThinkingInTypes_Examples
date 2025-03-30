# messenger.py
from dataclasses import dataclass, replace

@dataclass
class Messenger:
    name: str
    number: int
    depth: float = 0.0  # Default argument

x = Messenger(name="x", number=9, depth=2.0)
m = Messenger("foo", 12, 3.14)
print(m)
## Messenger(name='foo', number=12, depth=3.14)
print(m.name, m.number, m.depth)
## foo 12 3.14
mm = Messenger("xx", 1)  # Uses default argument
print(mm == Messenger("xx", 1))  # Generates __eq__()
## True
print(mm == Messenger("xx", 2))
## False

# Make a copy with a different depth:
mc = replace(m, depth=9.9)
print(m, mc)
## Messenger(name='foo', number=12, depth=3.14)
## Messenger(name='foo', number=12, depth=9.9)

# Mutable:
m.name = "bar"
print(m)
## Messenger(name='bar', number=12, depth=3.14)
# d = {m: "value"}
# TypeError: unhashable type: 'Messenger'
