from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.transacoes import Transacoes


class IItemRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transacoes]:
        pass

        
        