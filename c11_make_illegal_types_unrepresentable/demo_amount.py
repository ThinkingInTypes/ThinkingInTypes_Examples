# demo_amount.py
from decimal import Decimal

from amount import Amount
from book_utils import Catch

print(Amount.of(123))  # int
## Amount(value=Decimal('123'))
print(Amount.of("123"))  # str
## Amount(value=Decimal('123'))
print(Amount.of(1.23))  # float
## Amount(value=Decimal('1.23'))
print(Amount(Decimal("12.34")))
## Amount(value=Decimal('12.34'))
with Catch():
    Amount.of("not-a-number")
## Error: [<class 'decimal.ConversionSyntax'>]
