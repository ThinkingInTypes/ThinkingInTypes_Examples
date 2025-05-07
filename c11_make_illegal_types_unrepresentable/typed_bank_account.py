# typed_bank_account.py
from dataclasses import dataclass

from amount import Amount
from balance import Balance
from book_utils import Catch


@dataclass
class BankAccount:
    balance: Balance

    def deposit(self, amount: Amount) -> str:
        self.balance = self.balance.deposit(amount)
        return (
            f"Deposited {amount.value}, "
            f"Balance: {self.balance.amount.value}"
        )

    def withdraw(self, amount: Amount) -> str:
        self.balance = self.balance.withdraw(amount)
        return (
            f"Withdrew {amount.value}, "
            f"Balance: {self.balance.amount.value}"
        )


account = BankAccount(Balance(Amount.of(100)))
print(account.deposit(Amount.of(50)))
## Deposited 50, Balance: 150
print(account.withdraw(Amount.of(30)))
## Withdrew 30, Balance: 120
with Catch():
    account.withdraw(Amount.of(200))
## Error: Negative Amount(-80)
with Catch():
    account.deposit(Amount.of(-10))
## Error: Negative Amount(-10)
