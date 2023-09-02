from decimal import Decimal
from src.app.entities.transactions import Transactions
from ...enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM


class TransactionsDynamoDto:
    type_transaction:  TRANSACTIONS_TYPE_ENUM
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type_transaction:  TRANSACTIONS_TYPE_ENUM, value: float, current_balance: float, timestamp: float):
        self.type_transaction = type_transaction
        self.value = value
        self.current_balance = current_balance
        self.timestamp = timestamp

    @staticmethod
    def from_entity(transactions: Transactions) -> "TransactionsDynamoDto":
        return TransactionsDynamoDto(
            type_transaction=transactions.type_transaction,
            value=transactions.value,
            current_balance=transactions.current_balance,
            timestamp=transactions.timestamp,
        )

    def to_dynamo(self) -> dict:
        return {
            "type_transaction": self.type_transaction.value,
            'entity': 'transactions',
            "value": Decimal(str(self.value)),
            "current_balance": Decimal(str(self.current_balance)),
            "timestamp": Decimal(str(self.timestamp)),
        }
