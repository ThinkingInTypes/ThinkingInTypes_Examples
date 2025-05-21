# return_self.py
"""
Return `Self` enables type-safe method chaining in subclasses 
without the complexity of F-bounded generics.
"""
from dataclasses import dataclass, field
from typing import Self


@dataclass
class Form:
    title: str = ""

    def set_title(self, title: str) -> Self:
        self.title = title
        return self


@dataclass
class ContactForm(Form):
    fields: list[str] = field(default_factory=list)

    def add_field(self, name: str) -> Self:
        self.fields.append(name)
        return self


form = ContactForm().set_title("Feedback").add_field("email")
