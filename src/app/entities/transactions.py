from ..errors.entity_errors import ParamNotValidated
from ..enums.transactions_type_enum import TransactionsTypeEnum

import time

class Transactions:
    type_transaction: TransactionsTypeEnum
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type_transaction: TransactionsTypeEnum, value: float, current_balance: float, timestamp: float):
        
        self.type_transaction = type_transaction

        if not self.validate_value(value):
            raise ParamNotValidated("value", "Value must be a float")
        if not self.validate_negative_value(value):
            raise ParamNotValidated("value", "Value must be a positive number")
        self.value = value

        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "Current balance must be a float")
        if not self.validate_negative_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "Current balance must be a positive number")
        self.current_balance = current_balance

        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "Timestamp must be a float")
        self.timestamp = timestamp   

    def validate_negative_value(self, value: float) -> bool:
        return (value >= 0)

    def validate_value(sf, value: float) -> bool:
        return (type(value) == float)
    
    def validate_negative_current_balance(self, current_balance: float) -> bool:
        return current_balance >= 0

    def validate_current_balance(self, current_balance: float) -> bool:
        return (type(current_balance) == float)

    def validate_timestamp(self, timestamp: float) -> bool:
        return (type(timestamp) == float)

    def validate_transaction_type(self, type: TransactionsTypeEnum) -> bool:
        return (type(type) == TransactionsTypeEnum)
    
    
    def to_dict(self) -> dict:
        return {
            "type": self.type_transaction,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }

