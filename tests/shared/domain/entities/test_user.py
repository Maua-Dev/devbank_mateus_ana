import pytest

from src.shared.domain.entities.user import User
from src.shared.helpers.errors.entity_errors import ParamNotValidated



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
    
    def test_validate_len_name(self):
        name = ""
        with pytest.raises(ParamNotValidated):
            item = User(name, "0001", "12345-6", 1000.00)

    def test_validate_name(self):
        name = 8192
        with pytest.raises(ParamNotValidated):
            item = User(name, "0001", "12345-6", 1000.00)
    def test_validate_len_agency(self):
        agency = "000"
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", agency, "12345-6", 1000.00)
    def test_validate_agency(self):
        agency = 9021
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", agency, "12345-6", 1000.00)
    def test_validate_len_account(self):
        account = "123456"
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", "0001", account, 1000.00)
    def test_validate_account(self):
        account = 1234567
        with pytest.raises(ParamNotValidated):
            item =  User("Mateus", "0001", account, 1000.00)
    def test_validate_char_account(self):
        account = "1234-67"
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", "0001", account, 1000.00)
    def test_validate_current_balance(self):
        current_balance = "1000.00"
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", "0001", "12345-6", current_balance)
    def test_validate_negative_balance(self):
        current_balance = -1000.00
        with pytest.raises(ParamNotValidated):
            item = User("Mateus", "0001", "12345-6", current_balance)


    

