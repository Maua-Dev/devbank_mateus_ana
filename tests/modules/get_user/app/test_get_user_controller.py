from src.modules.get_user.app.get_user_controller import GetUserController
from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class Test_GetUserController:
    repo_mock = UserRepositoryMock()
    get_user_usecase = GetUserUsecase(repo_mock)
    controller = GetUserController(get_user_usecase)

    response = controller(HttpRequest(body={
        "name": "Mateus",
        "agency": "0000",
        "account": "12345-6",
        "current_balance": 1000
    }))
    assert response.status_code == 200