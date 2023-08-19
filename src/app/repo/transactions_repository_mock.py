from typing import Dict, Optional, List

from ..enums.transactions_type_enum import TransactionsTypeEnum
from ..entities.transactions import Transactions
from .transactions_repository_interface import IITransactionsRepository


class TransactionsRepositoryMock(IITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(type=TransactionsTypeEnum.DEPOSIT.value, value=1000.00, current_balance=1000.00, timestamp=1625548800.00),
            Transactions(type=TransactionsTypeEnum.DEPOSIT.value, value=2000.00, current_balance=3000.00, timestamp=1625548800.00),
            Transactions(type=TransactionsTypeEnum.WITHDRAW.value, value=500.00, current_balance=2500.00, timestamp=1625548800.00),
            Transactions(type=TransactionsTypeEnum.WITHDRAW.value, value=500.00, current_balance=2000.00, timestamp=1625548800.00),
        ]

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
    
    def create_transaction(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        
        return transaction
        
    
    