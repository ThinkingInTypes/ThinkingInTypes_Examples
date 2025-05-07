# phone_numbers_as_types.py
from phone_number import PhoneNumber
from string_phone_numbers import phone_numbers
from book_utils import Catch

for raw in phone_numbers:
    with Catch():
        pn = PhoneNumber.of(raw)
        print(f"{raw!r} -> {pn}")
## '5551234' -> +555 1234
## '555-1234' -> +555 1234
## '(555) 123-4567' -> +1 (555) 123-4567
## '555.123.4567' -> +555 1234567
## '+1-555-123-4567' -> +1 (555) 123-4567
## '+44 20 7946 0958' -> +44 (207) 946-0958
## '5551234567' -> +555 1234567
## '555 1234' -> +555 1234
## Error: Invalid phone number: '555-12ab'
## Error: Invalid phone number: 'CallMeMaybe'
## '01234' -> +012 34
## Error: Invalid phone number: ''
## ' 5551234 ' -> +555 1234
