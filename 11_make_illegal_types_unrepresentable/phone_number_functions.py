# phone_number_functions.py
from string_phone_numbers import phone_numbers
import re

def f1(phone: str):
    VALID = re.compile(r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$")
    if not VALID.match(phone):
        print(f"Error {phone = }")
        return
    ...

def f2(phone_num: str):
    CHECK = re.compile(r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$")
    assert CHECK.match(phone_num), f"Invalid {phone_num}"
    ...
