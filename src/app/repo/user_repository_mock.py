from typing import Dict, Optional, List

from src.app.repo.user_repository_interface import IUserRepository

from ..entities.user import User


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self.user = User(name="Mateus", agency="0000", account="12345-6", current_balance=1000.00)

    def get_user(self) -> User:
        return self.user

    def deposit_current_balance(self, current_balance: float) -> float:
        self.user.current_balance += current_balance
        return self.user    