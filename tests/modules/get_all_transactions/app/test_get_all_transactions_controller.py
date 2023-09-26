import time
from src.modules.get_all_transactions.app.get_all_transactions_controller import GetAllTransactionsController

from src.modules.get_all_transactions.app.get_all_transactions_usecase import GetAllTransactionsUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM


class Test_CreateTransactionController:
    repo_mock = TransactionsRepositoryMock()
    get_all_transactions_usecase = GetAllTransactionsUseCase(repo_mock)
    controller = GetAllTransactionsController(get_all_transactions_usecase)

    response = controller()
    
    assert response.status_code == 200