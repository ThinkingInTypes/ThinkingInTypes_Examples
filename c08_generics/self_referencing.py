# self_referencing.py
from __future__ import (
    annotations,
)  # For forward-referenced types
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Tree(Generic[T]):
    value: T
    children: list[Tree[T]] = field(default_factory=list)

    def add_child(self, child_value: T) -> Tree[T]:
        child = Tree(child_value)
        self.children.append(child)
        return child


root: Tree[str] = Tree("root")
child_node = root.add_child("child1")
grandchild = child_node.add_child("grandchild1")
