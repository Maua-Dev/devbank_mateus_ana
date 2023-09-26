
import time
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.modules.create_transaction.app.create_transaction_controller import CreateTransactionController
from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_CreateTransactionController:
    def test_create_transaction_controller(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)
        controller = CreateTransactionController(usecase)

        request={
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 1,
            "200": 0,
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT
        }   

        response = controller(request)

        assert response.status_code == 200
        assert response.body["type"] == transactions_repo.transactions[-1].type_transaction.value.lower()
        assert response.body["value"] == transactions_repo.transactions[-1].value
        assert response.body["current_balance"] == transactions_repo.transactions[-1].current_balance
        assert response.body['message'] == "Transaction created successfully"
    
    def test_create_transaction_controller_missing_type(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)
        controller = CreateTransactionController(usecase)

        request={
            "2": 0,
            "5": 0,
            "10": 0,
            "20": 0,
            "50": 0,
            "100": 1,
            "200": 0
        } 

        response = controller(request)

        assert response.status_code == 400

    def test_create_transaction_controller_missing_bill(self):
        transactions_repo = TransactionsRepositoryMock()
        user_repo = UserRepositoryMock()
        usecase = CreateTransactionUseCase(transactions_repo, user_repo)
        controller = CreateTransactionController(usecase)

        request={
            "2": 0,
            "5": 0,
            "10": 0,
            "50": 0,
            "100": 1,
            "200": 0,
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT.value.lower()
        }  

        response = controller(request)

        assert response.status_code == 400
    
   