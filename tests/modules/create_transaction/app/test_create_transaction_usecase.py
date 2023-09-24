import pytest

from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.shared.helpers.errors.entity_errors import ParamNotValidated
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_CreateTransactionUseCase:

    def test_create_transactions(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        request = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        transactions = usecase(
            type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            value=100.00,
            current_balance=1100.00,
            timestamp=1628400000.0,
            request=request
        )

        assert transactions == transactions_repo.transactions[-1]
    
    def test_create_transactions_with_invalid_type_transaction(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        request = {
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
                type_transaction="deposit",
                value=100.00,
                current_balance=1100.00,
                timestamp=1628400000.0,
                request=request
            )

    def test_create_transactions_with_invalid_value(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        request = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        with pytest.raises(ParamNotValidated):
            transactions = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value="100.00",
                current_balance=1100.00,
                timestamp=1628400000.0,
                request=request
            )
    
    def test_create_transactions_with_invalid_current_balance(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        request = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        with pytest.raises(ParamNotValidated):
            transactions = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value=100.00,
                current_balance="1100.00",
                timestamp=1628400000.0,
                request=request
            )
    
    def test_create_transactions_with_invalid_timestamp(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)

        request = {
            "2": 0,
            "5": 1,
            "10": 0,
            "20": 0,
            "50": 5,
            "100": 0,
            "200": 1
        }   

        with pytest.raises(ParamNotValidated):
            transactions = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value=100.00,
                current_balance=1100.00,
                timestamp="1628400000.0",
                request=request
            )