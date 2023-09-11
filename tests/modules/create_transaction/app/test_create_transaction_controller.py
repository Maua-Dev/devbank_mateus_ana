
import time
from src.modules.create_transaction.app.create_transaction_controller import CreateTransactionController
from src.modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_CreateTransactionController:
    def test_create_transaction_controller(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": 100.00,
            "current_balance": 1100.00,
            "timestamp": time.time(),
            "message": "Transaction created successfully"
        })

        response = controller(request)

        assert response.status_code == 200
        assert response.body["type"] == repo.transactions[0].type_transaction.value.lower()
        assert response.body["value"] == repo.transactions[0].value
        assert response.body["current_balance"] == repo.transactions[0].current_balance
        assert response.body['message'] == "Transaction created successfully"
    
    def test_create_transaction_controller_missing_type(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "value": 100.00,
            "current_balance": 1100.00,
            "timestamp": 1239.00,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field type is missing"

    def test_create_transaction_controller_missing_value(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "current_balance": 1100.00,
            "timestamp": 1239.00,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field value is missing"
    
    def test_create_transaction_controller_missing_current_balance(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": 100.00,
            "timestamp": 1239.00,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field current_balance is missing"

    def test_create_transaction_controller_missing_timestamp(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": 100.00,
            "current_balance": 1100.00,
        })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field timestamp is missing"
    
    def test_create_transaction_controller_invalid_value(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": "100.00",
            "current_balance": 1100.00,
            "timestamp": 1239.00,
        })

        response = controller(request)
        assert response.status_code == 500
    
    def test_create_transaction_controller_invalid_current_balance(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": 100.00,
            "current_balance": "1100.00",
            "timestamp": 1239.00,
        })

        response = controller(request)
        assert response.status_code == 500
    
    def test_create_transaction_controller_invalid_timestamp(self):
        repo = TransactionsRepositoryMock()
        usecase = CreateTransactionUseCase(repo)
        controller = CreateTransactionController(usecase)

        request = HttpRequest(body={
            "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            "value": 100.00,
            "current_balance": 1100.00,
            "timestamp": "1239.00",
        })

        response = controller(request)
        assert response.status_code == 500
        
