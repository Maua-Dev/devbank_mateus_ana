from fastapi.exceptions import HTTPException
import pytest


from src.app.main import get_all_transactions, get_user,deposit,withdraw


class Test_Main:

    def test_get_user(self):
        response = get_user()

        expected_response = {
            'name': 'Mateus',
            'agency': '0000',
            'account': '12345-6',
            'current_balance':1000.00
        }
        assert type(response) == dict
        assert response == expected_response

    def test_get_history(self):
        response = get_all_transactions()
        assert type(response) == dict
    
    def test_deposit(self):
        user = get_user()
        transactions = get_all_transactions()
        dict_values={
        "2": 5,
        "5": 0,
        "10": 0,
        "20": 3,
        "50": 1,
        "100": 0,
        "200": 0,
        }        
        response = deposit(dict_values)
        assert response["current_balance"] == user["current_balance"] + 120.0

    def test_withdraw(self):
        user = get_user()
        transactions = get_all_transactions()
        dict_values={
        "2": 5,
        "5": 0,
        "10": 0,
        "20": 3,
        "50": 1,
        "100": 0,
        "200": 0,
        }  
        response = withdraw(dict_values)
        
        assert response["current_balance"] == user["current_balance"] - 120.0

    
    