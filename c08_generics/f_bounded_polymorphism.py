# f_bounded_polymorphism.py
from __future__ import annotations
from typing import TypeVar, Generic

TSelf = TypeVar("TSelf", bound="Form")


class Form(Generic[TSelf]):
    def set_title(self: TSelf, title: str) -> TSelf:
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
