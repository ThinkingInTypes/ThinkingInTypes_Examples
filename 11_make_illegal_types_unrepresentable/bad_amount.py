# bad_amount.py
from amount import Amount
from book_utils import Catch

print(Amount(123))
## Amount(value=Decimal('123'))
print(Amount("123"))
## Amount(value=Decimal('123'))
print(Amount(1.23))
## Amount(value=Decimal('1.23'))
with Catch():
    Amount("not-a-number")
## Error: [<class 'decimal.ConversionSyntax'>]
