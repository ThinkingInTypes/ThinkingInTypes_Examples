# bank_account.py
from dataclasses import dataclass
from decimal import Decimal

from book_utils import Catch
from require import requires, Condition
from amount import Amount

positive_amount = Condition(
    check=lambda self, amount: amount >= Decimal("0"),
    message="Amount cannot be negative",
)

sufficient_balance = Condition(
    check=lambda self, amount: self.balance >= amount,
    message="Insufficient balance"
)


@dataclass
class BankAccount:
    balance: Decimal

    @requires(positive_amount, sufficient_balance)
    def withdraw(self, amount: Decimal) -> str:
        self.balance -= amount
        return f"Withdrew {amount}, balance: {self.balance}"

    @requires(positive_amount)
    def deposit(self, amount: Decimal) -> str:
        self.balance += amount
        return f"Deposited {amount}, balance: {self.balance}"


account = BankAccount(Decimal(100))
print(account.deposit(Decimal(50)))
print(account.withdraw(Decimal(30)))
with Catch():
    account.withdraw(Decimal(200))
with Catch():
    account.deposit(Decimal(-10))
