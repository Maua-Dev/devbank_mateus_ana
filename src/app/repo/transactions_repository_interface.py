from abc import ABC, abstractmethod
from typing import List

from ..entities.transactions import Transactions


class IITransactionsRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass

    def create_transaction(self, transaction: Transactions) -> Transactions:
        pass
    

        
        