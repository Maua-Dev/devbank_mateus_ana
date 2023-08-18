from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.transacoes import Transacoes
from .transacoes_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    transacoes: list[Transacoes]

    def __init__(self):
        self.transacoes = [
            Transacoes(type="deposit", value=1000, current_balance=1000, timestamp=1625548800),
            Transacoes(type="deposit", value=2000, current_balance=3000, timestamp=1625548800),
            Transacoes(type="withdraw", value=500, current_balance=2500, timestamp=1625548800),
            Transacoes(type="withdraw", value=500, current_balance=2000, timestamp=1625548800),
        ]

    def get_all_transactions(self) -> List[Transacoes]:
        return self.transacoes  
        
    
    