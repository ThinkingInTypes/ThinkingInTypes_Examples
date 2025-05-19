# f_bounded_polymorphism.py
from __future__ import annotations


class Form[T]:
    def set_title(self: T, title: str) -> T:
        self.title = title
        return self


class ContactForm(Form["ContactForm"]):
    def __init__(self):
        self.title = ""
        self.fields = []

    def add_field(self, name: str) -> ContactForm:
        self.fields.append(name)
        return self


form = ContactForm().set_title("Feedback").add_field("email")
