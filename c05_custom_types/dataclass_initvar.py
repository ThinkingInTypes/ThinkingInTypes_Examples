# dataclass_initvar.py
# pyright: reportAttributeAccessIssue=false
# mypy: disable-error-code="attr-defined"
from dataclasses import dataclass, InitVar
from book_utils import Catch


@dataclass
class Book:
    title: str
    author: str
    condition: InitVar[str]
    shelf_id: int | None = None

    def __post_init__(self, condition):
        if condition == "Unacceptable":
            self.shelf_id = None


print(b := Book("Emma", "Jane Austen", "Good", 11))
## Book(title='Emma', author='Jane Austen',
## shelf_id=11)
# "condition" doesn't exist outside __init__ or __post_init__:
with Catch():
    print(b.condition)  # noqa
