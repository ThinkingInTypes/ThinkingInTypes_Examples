# demo_amount.py
from decimal import Decimal

from amount import Amount
from book_utils import Catch

print(Amount.of(123))  # int
print(Amount.of("123"))  # str
print(Amount.of(1.23))  # float
print(Amount(Decimal("12.34")))
with Catch():
    Amount.of("not-a-number")
## Error: [<class 'decimal.ConversionSyntax'>]
