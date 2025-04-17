# team_post_init.py
from dataclasses import dataclass, field
from typing import List


@dataclass
class Team:
    leader: str
    members: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.leader = self.leader.capitalize()
        if self.leader not in self.members:
            self.members.insert(0, self.leader)


print(Team("alice", ["bob", "carol", "ted"]))
