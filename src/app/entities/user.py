class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str, agency: str, account: str, current_balance: float): 
        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = current_balance
    