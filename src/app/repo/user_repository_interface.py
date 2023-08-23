from abc import ABC, abstractmethod
from typing import List, Optional, Tuple


from ..entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> User:
        pass

    """Method: Function get_user returns an user object of class User"""

    def deposit_current_balance(self, current_balance: float) -> float:
        pass

    """Method: Function deposit_current_balance receives an type float variable(current_balance) that references user's account current balance and return an update of this variable (current_balance + deposit  = current_balance) as a type float too."""
    
    def withdraw_current_balance(self, current_balance:float) -> float:
        pass

    """Method: Function withdraw_current_balance receives an type float variable (current_balance) that references user's account current balance and return an update of this variable(current_balance - withdraw  = current_balance) as type float too."""