from typing import Tuple
from ...helpers.errors.entity_errors import ParamNotValidated
from..enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

import time

class Transactions:
    type_transaction:  TRANSACTIONS_TYPE_ENUM
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type_transaction:  TRANSACTIONS_TYPE_ENUM, value: float, current_balance: float, timestamp: float):
        

        if not self.validate_type_transaction(type_transaction):
            raise ParamNotValidated("type_transaction", "Type transaction must be a TRANSACTIONS_TYPE_ENUM")
        self.type_transaction = type_transaction

        validate_value = self.validate_value(value)
        if validate_value[0] is False:
            raise ParamNotValidated("value", validate_value[1])
        self.value = value

        validate_current_balance = self.validate_current_balance(current_balance)
        if validate_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validate_current_balance[1])
        self.current_balance = current_balance

    
        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "Timestamp must be a float")
        self.timestamp = timestamp   

    @staticmethod
    def validate_type_transaction(type_transaction:  TRANSACTIONS_TYPE_ENUM) -> bool:
        return (type(type_transaction) ==  TRANSACTIONS_TYPE_ENUM)

    
    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
        if type(value) != float:
            return(False, "Value must be a float")
        if value < 0:
            return (False, "Value must be a positive number")
        
        return(True, "")
        
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if type(current_balance) != float:
            return(False, "Value must be a float")
        if current_balance < 0:
            return(False, "Value must be a positive number")
        
        return(True, "")
    
    def validate_timestamp(self, timestamp: float) -> bool:
        return (type(timestamp) == float)
    

    def to_dict(self) -> dict:
        return {
            "type": self.type_transaction.value.lower(),
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }

