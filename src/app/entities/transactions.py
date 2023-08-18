from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class Transactions:
    type: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type: str, value: float, current_balance: float, timestamp: float):
        if not self.validate_string_type(type):
            raise ParamNotValidated("type", "Type must be a deposit or withdraw")
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

    def validate_string_type(self,type: str) -> bool:
        return (type == "deposit" or type == "withdraw")
    
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
    
        