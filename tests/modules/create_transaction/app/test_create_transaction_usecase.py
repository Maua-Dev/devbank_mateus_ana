import pytest

from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.shared.helpers.errors.entity_errors import ParamNotValidated
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_CreateTransactionUseCase:

    def test_create_transactions(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        dict_values = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        transactions = usecase(
            type=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            request=dict_values
        )

        assert transactions == transactions_repo.transactions[-1]
    
    def test_create_transactions_with_invalid_type_transaction(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        dict_values = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        with pytest.raises(ParamNotValidated):
            user = usecase(
                type="deposit",
                request=dict_values
            )

    def test_create_transactions_with_invalid_request(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        dict_values = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "200": 1
        }   

        with pytest.raises(ForbiddenAction):
            transactions = usecase(
                type=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                request=dict_values
            )
    
    