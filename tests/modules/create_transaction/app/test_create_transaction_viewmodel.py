from src.modules.create_transaction.app.create_transaction_viewmodel import CreateTransactionViewModel
from src.shared.domain.entities.transactions import Transactions
from src.shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

class Test_CreateTransactionViewModel:
    def test_create_transaction_viewmodel(self):
        transaction = Transactions(
            type_transaction=TRANSACTIONS_TYPE_ENUM.DEPOSIT,
            value=100.00,
            current_balance=100.00,
            timestamp=100.00
        )
        create_transaction_viewmodel = CreateTransactionViewModel(transaction).to_dict()
        assert create_transaction_viewmodel == {
            "type": "deposit",
            "value": 100.00,
            "current_balance": 100.00,
            "timestamp": 100.00,
            "message": "Transaction created successfully"
        }