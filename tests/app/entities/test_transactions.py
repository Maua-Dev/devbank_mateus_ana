import pytest

from src.app.entities.transactions import Transactions
from src.app.errors.entity_errors import ParamNotValidated



class Test_Transactions:
    def test_transactions(self):
        type = "deposit"
        value = 100.00
        current_balance = 100.00
        timestamp = 1004901390.00

        assert Transactions(type, value, current_balance, timestamp).type == type

    def test_validate_type(self):
        type = "aijwhdjias"

        with pytest.raises(ParamNotValidated):
            Transactions(type, 100.00, 100.00, 1004901390.00)

    def test_validate_value(self):
        value = "100.00"

        with pytest.raises(ParamNotValidated):
            Transactions("deposit", value, 100.00, 1004901390.00)

    def test_validate_negative_value(self):
        value = -100.00

        with pytest.raises(ParamNotValidated):
            Transactions("deposit", value, 100.00, 1004901390.00)
    
    def test_validate_current_balance(self):
        current_balance = "100.00"

        with pytest.raises(ParamNotValidated):
            Transactions("deposit", 100.00, current_balance, 1004901390.00)
    
    def test_validate_negative_current_balance(self):
        current_balance = -100.00

        with pytest.raises(ParamNotValidated):
            Transactions("deposit", 100.00, current_balance, 1004901390.00)
    
    def test_validate_timestamp(self):
        timestamp = "1004901390.00"

        with pytest.raises(ParamNotValidated):
            Transactions("deposit", 100.00, 100.00, timestamp)
