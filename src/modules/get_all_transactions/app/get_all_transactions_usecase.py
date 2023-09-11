from typing import List

from src.shared.domain.entities.transactions import Transactions
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.domain.repositories.transactions_repository_interface import ITransactionsRepository


class GetAllTransactionsUseCase:
    def __init__(self, repo: ITransactionsRepository):
        self.repo = repo
    
    def __call__(self) -> List[Transactions]:
        return self.repo.get_all_transactions()
