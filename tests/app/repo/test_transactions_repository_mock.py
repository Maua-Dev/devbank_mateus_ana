import pytest
from src.app.repo.transactions_repository_mock import ItemRepositoryMock


class Test_TransactionsRepositoryMock:
    def test_get_all_transactions(self):
        repo = ItemRepositoryMock()

        transactions = repo.get_all_transactions()

        expected_transactions = repo.transactions

        assert transactions == expected_transactions