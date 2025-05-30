# self_referencing.py
# For forward-referenced types:
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Tree[T]:
    value: T
    children: list[Tree[T]] = field(default_factory=list)

    def add_child(self, child_value: T) -> Tree[T]:
        child = Tree(child_value)
        self.children.append(child)
        return child


root: Tree[str] = Tree("root")
child_node = root.add_child("child1")
grandchild = child_node.add_child("grandchild1")
