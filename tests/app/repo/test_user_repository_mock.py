

from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
        repo = UserRepositoryMock()

        user = repo.get_user()

        expected_user = repo.user

        assert user == expected_user