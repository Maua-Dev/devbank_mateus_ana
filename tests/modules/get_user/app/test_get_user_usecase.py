import pytest

from src.modules.get_user.app.get_user_usecase import GetUserUsecase
from src.shared.helpers.errors.entity_errors import ParamNotValidated
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetUserUsecase:

    def test_get_user(self):
        repo = UserRepositoryMock()
        usecase = GetUserUsecase(repo)

        user = usecase()

        assert user == repo.user
