import pytest

from src.app.entities.transactions import Transactions



class Test_Transactions:
    def test_transactions(self):
        type = "deposit"
        value = 100.00
        current_balance = 100.00
        timestamp = 1004901390.00

        assert Transactions(type, value, current_balance, timestamp).type == type