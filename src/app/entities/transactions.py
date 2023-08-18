from ..errors.entity_errors import ParamNotValidated
from ..enums.transactions_type_enum import TransactionsTypeEnum

import time

class Transactions:
    type: TransactionsTypeEnum
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type: TransactionsTypeEnum, value: float, current_balance: float, timestamp: float):
        
        self.type = type

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

    def deposit(self, total_value: dict):
        if not self.validate_deposit(total_value):
            raise ParamNotValidated("total_value", "Total value must have some value to deposit")
        
        total_deposit = 0
        for k,v in total_value.items():
            value_bill = int(k)*v
            total_deposit += float(value_bill)
        
        if not self.validate_suspicious_deposit(total_value):
            raise ParamNotValidated("total_value", "Suspicious deposit")
        self.current_balance += total_deposit
        new_transaction = Transactions(
            type =  TransactionsTypeEnum.DEPOSIT,
            value = total_deposit,
            current_balance = self.current_balance,
            timestamp = round(time.time()*1000)
        )
        return new_transaction

    def validate_deposit(self, total_value: dict):
        return total_value != {}


    def validate_suspicious_deposit(self, total_value: dict):
        return sum(total_value.values()) > self.current_balance*2

    def to_dict(self) -> dict:
        return {
            "type": self.type.value,
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }


    
        