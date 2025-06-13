# f_bounded_polymorphism.py
from dataclasses import dataclass, field
from typing import cast


@dataclass
class Form[T]:
    title: str = ""

    def set_title(self, title: str) -> T:
        self.title = title
        # Returns self as type T for fluent chaining:
        return cast(T, self)


@dataclass
class ContactForm(Form["ContactForm"]):
    fields: list[str] = field(default_factory=list)

    def add_field(self, name: str) -> ContactForm:
        self.fields.append(name)
        return self


form = ContactForm().set_title("Feedback").add_field("email")
