from abc import ABC, abstractmethod
from typing import List, Optional, Tuple


from ..entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_user(self) -> User:
        pass

    """GET user 
    
    Parameters
    --------------------
    self:self

    Returns
    --------------------
    Object 

    {name == "Mateus"
    agency == "0001"
    account == "12345-6"
    current_balance == 1000.00}

    
    """

    def deposit_current_balance(self, current_balance: float) -> float:
        pass

    """
    Deposit current balance

    Paramenters
    -----------------------
    self: self
    current_balance: float
                    current_balance

    Returns
    --------------------------------
    float

        updates variable current_balance = current_balance + deposit_value
    """
    def withdraw_current_balance(self, current_balance:float) -> float:
        pass


    """
    Withdraw current balance

    Paramenters
    -----------------------
    self: self
    current_balance: float
                    current_balance

    Returns
    --------------------------------
    float

        updates variable current_balance = current_balance + withdraw_value
    """