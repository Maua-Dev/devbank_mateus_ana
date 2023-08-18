from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.transacoes import Item
from .item_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    def test(self):
        pass
        
    
    