from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from ....shared.domain.repositories.transactions_repository_interface import ITransactionsRepository
from ....shared.helpers.errors.entity_errors import ParamNotValidated


class CreateTransactionUseCase:
    def __init__(self, repo: ITransactionsRepository):
        self.repo = repo
    def __call__(self, type_transaction: TRANSACTIONS_TYPE_ENUM, value: float, current_balance: float, timestamp: float) -> Transactions:

        if not Transactions.validate_type_transaction(type_transaction):
            raise ParamNotValidated("type_transaction", "Type transaction must be a TRANSACTIONS_TYPE_ENUM")
        
        if not Transactions.validate_value(value)[0]:
            raise ParamNotValidated("value", Transactions.validate_value(value)[1])
        
        if not Transactions.validate_current_balance(current_balance)[0]:
            raise ParamNotValidated("current_balance", Transactions.validate_current_balance(current_balance)[1])
        
        if not Transactions.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "Timestamp must be a float")
        
        transaction = Transactions(
            type_transaction=type_transaction,
            value=value,
            current_balance=current_balance,
            timestamp=timestamp
        )
        
        return self.repo.create_transaction(transaction)