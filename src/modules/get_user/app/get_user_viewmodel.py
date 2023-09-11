from ....shared.domain.entities.user import User

class GetUserViewModel:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, transaction: User):
        self.name = transaction.name
        self.agency = transaction.agency
        self.account = transaction.account
        self.current_balance = transaction.current_balance
    
    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }