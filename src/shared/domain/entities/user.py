from abc import ABC

from typing import Tuple
from ...helpers.errors.entity_errors import ParamNotValidated 

class User(ABC):
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None): 

        validate_name = self.validate_name(name)
        if validate_name[0] is False:
            raise ParamNotValidated("name", validate_name[1])
        self.name = name
        
        validate_agency = self.validate_agency(agency)
        if validate_agency[0] is False:
            raise ParamNotValidated("agency", validate_agency[1])

        self.agency = agency
        
        validate_account = self.validate_account(account)
        if validate_account[0] is False:
            raise ParamNotValidated("account", validate_account[1])
        
        self.account = account

        validate_current_balance = self.validate_current_balance(current_balance)
        if validate_current_balance[0] is False:
            raise ParamNotValidated("Current_balance", validate_current_balance[1])
        
        self.current_balance = current_balance
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool,str]:
        if type(name) != str:
            return(False,  "Name must be a string")
        if len(name) <= 0:
            return(False, "Name must be filled")
        
        return(True, "")
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if type(agency) != str:
            return(False, "Agency must be a string")
        
        if len(agency) != 4:
            return(False, "Agency must have 4 characters")
        
        return(True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if type(account) != str:
            return(False, "Account must be a string" )
        
        if len(account) != 7:
            return(False, "Account must have 7 characters" )
        
        if account[5] != "-":
            return(False,"Account must have 5th character as '-'" )
        
        return(True, "")
    
    @staticmethod
    def validate_current_balance(current_balance:float) -> Tuple[bool, str]:
        if type(current_balance) != float:
            return(False,"Current balance must be a float" )
        
        if current_balance < 0:
            return(False, "Current balance must be a positive number")
        
        return(True, "")
 
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
