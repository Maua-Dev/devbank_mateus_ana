from src.modules.get_all_transactions.app.get_all_transactions_viewmodel import GetAllTransactionsViewModel
from src.shared.domain.entities.transactions import Transactions
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_GetAllTransactionsViewModel:
    all_transactions = [
        Transactions(
            type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            value=100.00,
            current_balance=100.00,
            timestamp=100.00
        ),
        Transactions(
            type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            value=100.00,
            current_balance=200.00,
            timestamp=200.00
        )
    ]

    def test_get_all_transactions_viewmodel(self):
        viewmodel = GetAllTransactionsViewModel(self.all_transactions).to_dict()

        assert viewmodel == {
            "all_transactions": [
                {
                    "type_transaction": "deposit",
                    "value": 100.00,
                    "current_balance": 100.00,
                    "timestamp": 100.00
                },
                {
                    "type_transaction": "deposit",
                    "value": 100.00,
                    "current_balance": 200.00,
                    "timestamp": 200.00
                }
            ]
        }
    
    