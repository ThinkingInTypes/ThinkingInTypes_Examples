# default_factory.py
from dataclasses import dataclass, field
from typing import List, Dict

_n = 0


def next_ten() -> int:
    global _n
    _n += 10
    return _n


@dataclass
class UserProfile:
    username: str
    # Built-in factory: each instance gets a new empty list
    strlist: List[str] = field(default_factory=list)
    n1: int = field(default_factory=next_ten)
    data: Dict[str, str] = field(
        default_factory=lambda: {"A": "B"}
    )
    n2: int = field(default_factory=next_ten)


print(user1 := UserProfile("Alice"))
## UserProfile(username='Alice', strlist=[], n1=10, data={'A': 'B'},
## n2=20)
print(user2 := UserProfile("Bob"))
## UserProfile(username='Bob', strlist=[], n1=30, data={'A': 'B'},
## n2=40)

# Modify mutable fields to verify they don't share state
user1.strlist.append("dark_mode")
user2.strlist.append("notifications")
user2.data["C"] = "D"
print(f"{user1 = }")
## user1 = UserProfile(username='Alice', strlist=['dark_mode'],
## n1=10, data={'A': 'B'}, n2=20)
print(f"{user2 = }")
## user2 = UserProfile(username='Bob', strlist=['notifications'],
## n1=30, data={'A': 'B', 'C': 'D'}, n2=40)
