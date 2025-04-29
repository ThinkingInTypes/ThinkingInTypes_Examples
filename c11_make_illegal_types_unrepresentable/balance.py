# balance.py
from __future__ import annotations
from typing import NamedTuple
from amount import Amount


class Balance(NamedTuple):
    amount: Amount

    def deposit(self, amount: Amount) -> Balance:
        return Balance(self.amount + amount)

    def withdraw(self, amount: Amount) -> Balance:
        return Balance(self.amount - amount)
