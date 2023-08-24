import pytest

from src.app.entities.transactions import Transactions
from src.app.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

from src.app.errors.entity_errors import ParamNotValidated




class Test_Transactions:
    def test_transactions(self):
        type =  TRANSACTIONS_TYPE_ENUM.WITHDRAW.value
        value = 100.00
        current_balance = 100.00
        timestamp = 1004901390.00

        assert Transactions(type, value, current_balance, timestamp).type_transaction == type

    def test_validate_value(self):
        value = "100.00"

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.DEPOSIT.value, value, 100.00, 1004901390.00)
        
        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.WITHDRAW.value,
            value, 100.00, 1004901390.00)

    def test_validate_negative_value(self):
        value = -100.00

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.DEPOSIT.value, value, 100.00, 1004901390.00)
        
        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.WITHDRAW.value,
            value, 100.00, 1004901390.00)
    
    def test_validate_current_balance(self):
        current_balance = "100.00"

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.DEPOSIT.value, 100.00, current_balance, 1004901390.00)

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.WITHDRAW.value,
            100.00, current_balance, 1004901390.00)
    
    def test_validate_negative_current_balance(self):
        current_balance = -100.00

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.DEPOSIT.value, 100.00, current_balance, 1004901390.00)

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.WITHDRAW.value,
            100.00, current_balance, 1004901390.00)
    
    def test_validate_timestamp(self):
        timestamp = "1004901390.00"

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.DEPOSIT.value, 100.00, 100.00, timestamp)

        with pytest.raises(ParamNotValidated):
            Transactions( TRANSACTIONS_TYPE_ENUM.WITHDRAW.value, 100.00, 100.00, timestamp)
