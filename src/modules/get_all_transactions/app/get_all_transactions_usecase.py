from typing import List

from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.repositories.transactions_repository_interface import ITransactionsRepository


class GetAllTransactionsUseCase:
    def __init__(self, repo: ITransactionsRepository):
        self.repo = repo
    
    def __call__(self) -> List[Transactions]:
        return self.repo.get_all_transactions()
