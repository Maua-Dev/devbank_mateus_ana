

from src.app.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock


class Test_UserRepositoryMock:
        repo_user = UserRepositoryMock()
        repo_transaction = TransactionsRepositoryMock()

        user = repo_user.get_user()
        transaction = repo_transaction.get_all_transactions()

        def test_get_user(self):
                expected_user = self.user
                assert self.user == expected_user
        
        def test_deposit_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == TRANSACTIONS_TYPE_ENUM.DEPOSIT:
                                expected_current_balance = self.user.current_balance + transaction.value
                                assert self.user.current_balance + transaction.value == expected_current_balance
        
        def test_withdraw_current_balance(self):
                for transaction in self.transaction:
                        if transaction.type_transaction == TRANSACTIONS_TYPE_ENUM.WITHDRAW:
                                expected_current_balance = self.user.current_balance - transaction.value
                                assert self.user.current_balance - transaction.value == expected_current_balance
        