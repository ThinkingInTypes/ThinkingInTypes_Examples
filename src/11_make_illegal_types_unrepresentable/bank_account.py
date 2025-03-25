# bank_account.py
from dataclasses import dataclass
from decimal import Decimal
from require import requires, Condition

positive_amount = Condition(
    check=lambda self, amount: amount >= Decimal("0"),
    message="Amount cannot be negative",
)

sufficient_balance = Condition(
    check=lambda self, amount: self.balance >= amount, message="Insufficient balance"
)


@dataclass
class BankAccount:
    balance: Decimal

    @requires(positive_amount, sufficient_balance)
    def withdraw(self, amount: Decimal) -> None:
        self.balance -= amount
        print(f"Withdrew {amount}, balance: {self.balance}")

    @requires(positive_amount)
    def deposit(self, amount: Decimal) -> None:
        self.balance += amount
        print(f"Deposited {amount}, balance: {self.balance}")


account = BankAccount(Decimal("100"))
account.deposit(Decimal("50"))
## Deposited 50, balance: 150
account.withdraw(Decimal("30"))
## Withdrew 30, balance: 120

try:
    account.withdraw(Decimal("200"))
except Exception as e:
    print(f"Error: {e}")
## Error: Insufficient balance

try:
    account.deposit(Decimal("-10"))
except Exception as e:
    print(f"Error: {e}")
## Error: Amount cannot be negative
