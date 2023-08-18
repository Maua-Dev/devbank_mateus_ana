import pytest
from src.app.entities.transacoes import Transacoes



class Test_Transacoes:
    def test_transacoes(self):
        type = "deposit"
        value = 100.00
        current_balance = 100.00
        timestamp = 1004901390.00

        assert Transacoes(type, value, current_balance, timestamp).type == type