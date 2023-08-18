from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.transacoes import Item


class IItemRepository(ABC):
    
    
    def test(self):
        pass