from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.entities.transactions import TRANSACTIONS_TYPE_ENUM

class CreateTransactionViewModel:
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
            "type": self.type_transaction.value.lower(),
            "value": self.value,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp,
            "message": "Transaction created successfully"
        }