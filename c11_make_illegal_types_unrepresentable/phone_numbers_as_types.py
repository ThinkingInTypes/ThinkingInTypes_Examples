# phone_numbers_as_types.py
from phone_number import PhoneNumber
from string_phone_numbers import phone_numbers
from book_utils import Catch

for raw in phone_numbers:
    with Catch():
        print(PhoneNumber.of(raw))
## +555 1234
## +555 1234
## +1 (555) 123-4567
## +555 1234567
## +1 (555) 123-4567
## +44 (207) 946-0958
## +555 1234567
## +555 1234
## Error: Invalid phone number: '555-12ab'
## Error: Invalid phone number: 'CallMeMaybe'
## +012 34
## Error: Invalid phone number: ''
## +555 1234
print(PhoneNumber("886", "7775551212"))
## +886 (777) 555-1212
