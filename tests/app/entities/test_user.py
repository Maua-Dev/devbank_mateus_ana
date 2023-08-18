import pytest

from src.app.entities.user import User



class Test_User:
    def test_users(self):
        name = "Mateus"
        agency = "0001"
        account = "12345-6"
        current_balance = 1000.00

        user = User(name, agency, account, current_balance)
        assert user.name == "Mateus"
        assert user.agency == "0001"
        assert user.account == "12345-6"
        assert user.current_balance == 1000.00

