import time
from typing import Dict, Optional, List
from ...domain.entities.transactions import Transactions
from ...domain.repositories.transactions_repository_interface import ITransactionsRepository
from ...domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM


class TransactionsRepositoryMock(ITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1628400000.0),
            Transactions(TRANSACTIONS_TYPE_ENUM.WITHDRAW, 50.00, 1050.00, time.time()*1000),
        ]
        
    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
    
    def create_transaction(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        return transaction
        
    
    