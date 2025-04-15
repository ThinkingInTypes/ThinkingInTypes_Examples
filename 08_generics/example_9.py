# example_9.py
from __future__ import annotations  # enable forward references in type hints (for Python < 3.11)
from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class Tree(Generic[T]):
    value: T
    children: list[Tree[T]] = field(default_factory=list)

    def add_child(self, child_value: T) -> Tree[T]:
        """Add a child node with the given value and return the new child"""
        child = Tree(child_value)
        self.children.append(child)
        return child

# Example usage:
root: Tree[str] = Tree("root")
child_node = root.add_child("child1")
grandchild = child_node.add_child("grandchild1")
