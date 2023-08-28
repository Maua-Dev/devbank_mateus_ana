import time
from typing import Dict, Optional, List
from ..entities.transactions import Transactions
from .transactions_repository_interface import IITransactionsRepository
from ..enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM


class TransactionsRepositoryMock(IITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, time.time()*1000),
            Transactions(TRANSACTIONS_TYPE_ENUM.WITHDRAW, 50.00, 1050.00, time.time()*1000),
        ]
        
    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
    
    def create_transaction(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        return transaction
        
    
    