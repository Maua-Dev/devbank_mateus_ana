

from src.app.repo.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:
    def test_get_user(self):
        repo = UserRepositoryMock()

        user = repo.get_user()

        expected_user = repo.user

        assert user == expected_user