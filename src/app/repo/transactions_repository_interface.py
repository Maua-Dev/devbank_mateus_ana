from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.transactions import Transactions


class IITransactionsRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass

    

        
        