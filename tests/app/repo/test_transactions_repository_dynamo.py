import pytest
from src.app.entities.transactions import Transactions
from src.app.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.app.repo.transactions_repository_dynamo import TransactionsRepositoryDynamo


class Test_TransactionsRepositoryDynamo:
    def test_get_all_transactions(self):
        pass

    @pytest.mark.skip("Cannot test in GitHub CI")
    def test_create_transaction(self):
        transaction = Transactions(
            TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693661969068.1855)

        repo_dynamo = TransactionsRepositoryDynamo()
        new_transactions = repo_dynamo.create_transaction(transaction)

        assert new_transactions == transaction
