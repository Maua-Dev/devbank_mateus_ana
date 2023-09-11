from typing import List

from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM


class TransactionsViewModel:
    type_transaction: TRANSACTIONS_TYPE_ENUM
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, transaction: Transactions):
        self.type_transaction = transaction.type_transaction
        self.value = transaction.value
        self.current_balance = transaction.current_balance
        self.timestamp = transaction.timestamp
    
    def to_dict(self):
        return {
            "type_transaction": self.type_transaction.value.lower(),
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }
    
class GetAllTransactionsViewModel:
    def __init__(self, transactions_list: List[Transactions]):
        self.transactions_viewmodel_list = [TransactionsViewModel(transaction).to_dict() for transaction in transactions_list]

    def to_dict(self):
        return {
            "all_transactions": self.transactions_viewmodel_list
        }