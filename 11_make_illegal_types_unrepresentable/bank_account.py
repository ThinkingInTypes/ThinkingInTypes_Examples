# bank_account.py
from dataclasses import dataclass
from decimal import Decimal
from require import requires, Condition
from book_utils import catch

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


account = BankAccount(Decimal("100"))
print(account.deposit(Amount("50")))
print(account.withdraw(Amount("30")))
catch(account.withdraw, Amount("200"))
catch(account.deposit, Amount("-10"))
