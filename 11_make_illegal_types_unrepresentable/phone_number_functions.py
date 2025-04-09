# phone_number_functions.py
import re


def f1(phone: str):
    valid = re.compile(
        r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$"
    )
    if not valid.match(phone):
        print(f"Error {phone = }")
        return
    ...


def f2(phone_num: str):
    check = re.compile(
        r"^\+?(\d{1,3})?[\s\-.()]*([\d\s\-.()]+)$"
    )
    assert check.match(phone_num), f"Invalid {phone_num}"
    ...
