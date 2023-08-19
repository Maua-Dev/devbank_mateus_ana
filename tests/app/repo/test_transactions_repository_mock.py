import pytest
from src.app.entities.transactions import Transactions
from src.app.enums.transactions_type_enum import TransactionsTypeEnum
from src.app.repo.transactions_repository_mock import TransactionsRepositoryMock


class Test_TransactionsRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionsRepositoryMock()

        transactions = repo.get_all_transactions()

        expected_transactions = repo.transactions

        assert transactions == expected_transactions
    
    def test_create_transaction(self):
        repo = TransactionsRepositoryMock()

        transaction = repo.create_transaction(
            Transactions(
                type=TransactionsTypeEnum.DEPOSIT.value,    
                value=1000.00,
                current_balance=1000.00,
                timestamp=1625548800.00
            )
        )

        assert transaction == repo.transactions[len(repo.transactions) - 1]