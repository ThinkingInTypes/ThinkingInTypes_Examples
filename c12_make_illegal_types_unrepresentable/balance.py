# balance.py
from dataclasses import dataclass
from amount import Amount


@dataclass(frozen=True)
class Balance:
    amount: Amount

    def deposit(self, amount: Amount) -> Balance:
        return Balance(self.amount + amount)

    def withdraw(self, amount: Amount) -> Balance:
        return Balance(self.amount - amount)
