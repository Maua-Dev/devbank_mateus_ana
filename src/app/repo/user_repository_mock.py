from typing import Dict, Optional, List

from src.app.repo.user_repository_interface import IUserRepository

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.user import User


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self.user = User(name="Mateus", agency="0000", account="12345-6", current_balance=1000.00)

    def get_user(self) -> List[User]:
        return self.user