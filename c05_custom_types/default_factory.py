# default_factory.py
from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime
import random


def current_time() -> datetime:
    return datetime.now()


def random_id() -> int:
    return random.randint(1000, 9999)


@dataclass
class UserProfile:
    username: str
    # Built-in factory ensures each instance gets a new empty list
    preferences: List[str] = field(default_factory=list)
    # Custom factory functions:
    created_at: datetime = field(default_factory=current_time)
    metadata: Dict[str, str] = field(default_factory=lambda: {"role": "user"})
    user_id: int = field(default_factory=random_id)


user1 = UserProfile("Alice")
user2 = UserProfile("Bob")

# Modify mutable fields to verify they don't share state
user1.preferences.append("dark_mode")
user2.preferences.append("notifications")
user2.metadata["role"] = "admin"
print(f"{user1 = }")
print(f"{user2 = }")
