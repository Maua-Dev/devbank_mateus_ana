from typing import Dict, Optional, List
from ..entities.transactions import Transactions
from .transactions_repository_interface import IITransactionsRepository


class TransactionsRepositoryMock(IITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = []

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
    
    def create_transaction(self, transaction: Transactions) -> Transactions:
        self.transactions.append(transaction)
        return transaction
        
    
    