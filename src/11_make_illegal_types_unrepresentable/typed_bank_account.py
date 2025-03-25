# typed_bank_account.py
from dataclasses import dataclass

from amount import Amount
from balance import Balance


@dataclass
class BankAccount:
    balance: Balance

    def deposit(self, amount: Amount) -> None:
        self.balance = self.balance.deposit(amount)
        print(f"Deposited {amount.value}, balance: {self.balance.amount.value}")

    def withdraw(self, amount: Amount) -> None:
        self.balance = self.balance.withdraw(amount)
        print(f"Withdrew {amount.value}, balance: {self.balance.amount.value}")


account = BankAccount(Balance(Amount(100)))
account.deposit(Amount(50))
## Deposited 50, balance: 150
account.withdraw(Amount(30))
## Withdrew 30, balance: 120

try:
    account.withdraw(Amount(200))  # Too much
except ValueError as e:
    print(f"Error: {e}")
## Error: Amount cannot be negative, got -80

try:
    account.deposit(Amount(-10))  # Invalid
except ValueError as e:
    print(f"Error: {e}")
## Error: Amount cannot be negative, got -10
