# typed_bank_account.py
from dataclasses import dataclass
from amount import Amount
from balance import Balance
from book_utils import catch


@dataclass
class BankAccount:
    balance: Balance

    def deposit(self, amount: Amount) -> str:
        self.balance = self.balance.deposit(amount)
        return f"Deposited {amount.value}, balance: {self.balance.amount.value}"

    def withdraw(self, amount: Amount) -> str:
        self.balance = self.balance.withdraw(amount)
        return f"Withdrew {amount.value}, balance: {self.balance.amount.value}"


account = BankAccount(Balance(Amount(100)))
print(account.deposit(Amount("50")))
print(account.withdraw(Amount("30")))
catch(account.withdraw, Amount("200"))
catch(account.deposit, Amount("-10"))
