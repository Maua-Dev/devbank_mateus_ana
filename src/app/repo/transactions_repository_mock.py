from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.transactions import Transactions
from .transactions_repository_interface import IITransactionsRepository


class ItemRepositoryMock(IITransactionsRepository):
    transactions: list[Transactions]

    def __init__(self):
        self.transactions = [
            Transactions(type="deposit", value=1000, current_balance=1000, timestamp=1625548800),
            Transactions(type="deposit", value=2000, current_balance=3000, timestamp=1625548800),
            Transactions(type="withdraw", value=500, current_balance=2500, timestamp=1625548800),
            Transactions(type="withdraw", value=500, current_balance=2000, timestamp=1625548800),
        ]

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions  
        
    
    