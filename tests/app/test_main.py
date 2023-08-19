from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.transactions import Transactions

from src.app.main import get_all_transactions, get_user


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
         
    
    