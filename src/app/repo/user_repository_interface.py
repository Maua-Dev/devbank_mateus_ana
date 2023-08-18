from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> List[User]:
        pass