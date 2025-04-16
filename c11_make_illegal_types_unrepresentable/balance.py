# balance.py
from typing import NamedTuple
from amount import Amount


class Balance(NamedTuple):
    amount: Amount

    def deposit(
            self, deposit_amount: Amount
    ) -> "Balance":
        return Balance(self.amount + deposit_amount)

    def withdraw(
            self, withdrawal_amount: Amount
    ) -> "Balance":
        return Balance(self.amount - withdrawal_amount)
