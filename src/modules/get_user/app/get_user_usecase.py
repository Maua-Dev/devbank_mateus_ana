from typing import Any
from ....shared.domain.entities.user import User
from ....shared.domain.repositories.user_repository_interface import IUserRepository

class GetUserUsecase:
    def __init__(self, repo: IUserRepository):
        self.repo = repo
    
    def __call__(self) -> User:
        return self.repo.get_user()