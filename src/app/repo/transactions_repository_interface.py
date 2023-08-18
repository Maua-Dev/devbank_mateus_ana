from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.transactions import Transactions


class IITransactionsRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass

    

        
        