import pytest
from src.app.entities.transactions import Transactions
from src.app.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock


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
                type_transaction= TRANSACTIONS_TYPE_ENUM.DEPOSIT,    
                value=1000.00,
                current_balance=1000.00,
                timestamp=1625548800.00
            )
        )
        if len(repo.transactions) > 0:
            assert transaction == repo.transactions[len(repo.transactions) - 1]
        else:
            assert transaction == repo.transactions[0]