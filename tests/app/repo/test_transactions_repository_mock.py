import pytest
from src.app.repo.transactions_repository_mock import TransactionsRepositoryMock


class Test_TransactionsRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionsRepositoryMock()

        transactions = repo.get_all_transactions()

        expected_transactions = repo.transactions

        assert transactions == expected_transactions