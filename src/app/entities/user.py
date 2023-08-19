from src.app.errors.entity_errors import ParamNotValidated

class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None): 
        if not self.validate_name(name):
            raise ParamNotValidated("name", "Name must be a string")
        if not self.validate_len_name(name):
            raise ParamNotValidated("name", "Name must be filled")
        self.name = name

        if not self.validate_agency(agency):
            raise ParamNotValidated("agency", "Agency must be a string")
        if not self.validate_len_agency(agency):
            raise ParamNotValidated("agency", "Agency must have 4 characters")
        self.agency = agency
        
        if not self.validate_account(account):
            raise ParamNotValidated("account", "Account must be a string")
        if not self.validate_len_account(account):
            raise ParamNotValidated("account", "Account must have 7 characters")
        if not self.validate_char_account(account):
            raise ParamNotValidated("account", "Account must have 5th character as '-'")
        self.account = account

        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "Current balance must be a float")
        if not self.validate_negative_balance(current_balance):
            raise ParamNotValidated("current_balance", "Current balance must be a positive number")
        self.current_balance = current_balance
    

    def validate_len_name(self, name: str) -> bool:
        return (len(name) > 0)
    
    def validate_name(self, name: str) -> bool:
        return (type(name) == str)
    
    
    def validate_len_agency(self, agency: str) -> bool:
        return (len(agency) == 4)
    
    
    def validate_agency(self, agency: str) -> bool:
        return (type(agency) == str)
    

    def validate_len_account(self, account: str) -> bool:
        return (len(account) == 7)
    

    def validate_account(self, account: str) -> bool:
        return (type(account) == str)
    

    def validate_char_account(self, account: str) -> bool:
        return (account[5] == "-")
    

    def validate_current_balance(self, current_balance: float) -> bool:
        return (type(current_balance) == float)
    

    def validate_negative_balance(self, current_balance: float) -> bool:
        return (current_balance >= 0)
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
