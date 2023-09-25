from src.app.main import get_all_transactions, get_user,deposit,withdraw
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.shared.helpers.external_interfaces.http_codes import OK


class Test_Main:

    def test_get_user(self):
        response = get_user()

        expected_response = {
            'name': 'Mateus',
            'agency': '0000',
            'account': '12345-6',
            'current_balance':1050.00
        }
        assert type(response) == OK
        assert response.body == expected_response

    def test_get_history(self):
        response = get_all_transactions()
        assert type(response) == OK
    
    def test_deposit(self):
        dict_values={
        "2": 5,
        "5": 0,
        "10": 0,
        "20": 3,
        "50": 1,
        "100": 0,
        "200": 0,
        "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT.value.lower()
        }        
        response = deposit(dict_values).body
        
        assert type(response) == dict

    def test_withdraw(self):
        dict_values={
        "2": 5,
        "5": 0,
        "10": 0,
        "20": 3,
        "50": 1,
        "100": 0,
        "200": 0,
        "type": TRANSACTIONS_TYPE_ENUM.WITHDRAW.value.lower()
        }  
        response = withdraw(dict_values).body

        assert type(response) == dict
        
        
    
    