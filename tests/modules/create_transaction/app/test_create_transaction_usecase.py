import pytest

from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.shared.helpers.errors.entity_errors import ParamNotValidated
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_CreateTransactionUseCase:

    def test_create_user(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)

        user = usecase(
            type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            value=100.00,
            current_balance=1100.00,
            timestamp=1628400000.0
        )

        assert user == repo.transactions[-1]
    
    def test_create_user_with_invalid_type_transaction(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)

        with pytest.raises(ParamNotValidated):
            user = usecase(
                type_transaction="deposit",
                value=100.00,
                current_balance=1100.00,
                timestamp=1628400000.0
            )

    def test_create_user_with_invalid_value(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)

        with pytest.raises(ParamNotValidated):
            user = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value="100.00",
                current_balance=1100.00,
                timestamp=1628400000.0
            )
    
    def test_create_user_with_invalid_current_balance(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)

        with pytest.raises(ParamNotValidated):
            user = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value=100.00,
                current_balance="1100.00",
                timestamp=1628400000.0
            )
    
    def test_create_user_with_invalid_timestamp(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)

        with pytest.raises(ParamNotValidated):
            user = usecase(
                type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
                value=100.00,
                current_balance=1100.00,
                timestamp="1628400000.0"
            )