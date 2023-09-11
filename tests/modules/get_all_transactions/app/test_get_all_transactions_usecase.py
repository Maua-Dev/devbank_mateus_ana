from src.modules.get_all_transactions.app.get_all_transactions_usecase import GetAllTransactionsUseCase
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_GetAllTransactionsUseCase:
    def test_get_all_transactions_use_case(self):
        repo_mock = TransactionsRepositoryMock()
        usecase = GetAllTransactionsUseCase(repo_mock)

        all_transactions = usecase()

        assert all_transactions == repo_mock.transactions