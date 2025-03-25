# typed_bank_account.py
from typing import NamedTuple
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Amount:
    value: Decimal

    def __init__(self, value: int | float | str | Decimal) -> None:
        decimal_value = Decimal(str(value))
        if decimal_value < Decimal("0"):
            raise ValueError(f"Amount cannot be negative, got {decimal_value}")
        object.__setattr__(self, "value", decimal_value)

    def __add__(self, other: "Amount") -> "Amount":
        return Amount(self.value + other.value)

    def __sub__(self, other: "Amount") -> "Amount":
        return Amount(self.value - other.value)


class Balance(NamedTuple):
    amount: Amount

    def deposit(self, deposit_amount: Amount) -> "Balance":
        return Balance(self.amount + deposit_amount)

    def withdraw(self, withdrawal_amount: Amount) -> "Balance":
        return Balance(self.amount - withdrawal_amount)


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
