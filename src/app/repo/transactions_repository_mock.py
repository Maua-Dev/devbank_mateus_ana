from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.transactions import Transactions
from .transactions_repository_interface import IITransactionsRepository


class ItemRepositoryMock(IITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(type="deposit", value=1000.00, current_balance=1000.00, timestamp=1625548800.00),
            Transactions(type="deposit", value=2000.00, current_balance=3000.00, timestamp=1625548800.00),
            Transactions(type="withdraw", value=500.00, current_balance=2500.00, timestamp=1625548800.00),
            Transactions(type="withdraw", value=500.00, current_balance=2000.00, timestamp=1625548800.00),
        ]

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
        
    
    