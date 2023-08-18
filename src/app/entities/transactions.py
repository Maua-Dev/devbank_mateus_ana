from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum


class Transactions:
    type: str
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type: str, value: float, current_balance: float, timestamp: float):
        self.type = type
        self.value = value
        self.current_balance = current_balance
        self.timestamp = timestamp        
    
        