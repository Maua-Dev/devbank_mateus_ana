from fastapi.exceptions import HTTPException

from ....shared.helpers.errors.usecase_errors import ForbiddenAction
from ....shared.helpers.enum.http_status_code_enum import HttpStatusCodeEnum
from ....shared.domain.repositories.user_repository_interface import IUserRepository
from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from ....shared.domain.repositories.transactions_repository_interface import ITransactionsRepository
from ....shared.helpers.errors.entity_errors import ParamNotValidated


class CreateTransactionUseCase:
    def __init__(self, repoTransaction: ITransactionsRepository, repoUser: IUserRepository):
        self.repoTransaction = repoTransaction
        self.repoUser = repoUser
    def __call__(self, type_transaction: TRANSACTIONS_TYPE_ENUM, value: float, current_balance: float, timestamp: float, request: dict) -> Transactions:
        if not Transactions.validate_type_transaction(type_transaction):
            raise ParamNotValidated("type_transaction", "Type transaction must be a TRANSACTIONS_TYPE_ENUM")
        
        if not Transactions.validate_value(value)[0]:
            raise ParamNotValidated("value", Transactions.validate_value(value)[1])
        
        if not Transactions.validate_current_balance(current_balance)[0]:
            raise ParamNotValidated("current_balance", Transactions.validate_current_balance(current_balance)[1])
        
        if not Transactions.validate_timestamp(self,timestamp=timestamp):
            raise ParamNotValidated("timestamp", "Timestamp must be a float")

        if request.keys() != {"2","5","10","20","50","100","200"}:
            raise ForbiddenAction("Request must be a dict with keys 2,5,10,20,50,100,200")

        
        transaction = Transactions(
            type_transaction=type_transaction,
            value=value,
            current_balance=current_balance,
            timestamp=timestamp
        )
        if transaction.type_transaction == TRANSACTIONS_TYPE_ENUM.DEPOSIT:
            if transaction.value > 2*self.repoUser.get_user().current_balance:
                raise ForbiddenAction("Suspicious transaction")
            if transaction.value <= 0:
                raise ForbiddenAction("Total deposit must be positive")
            self.repoUser.deposit_current_balance(transaction.value)
        else:
            if transaction.value > self.repoUser.get_user().current_balance:
                raise ForbiddenAction("Not enough balance")
            if transaction.value <= 0:
                raise ForbiddenAction("Total withdraw must be positive")
            self.repoUser.withdraw_current_balance(transaction.value)

        return self.repoTransaction.create_transaction(transaction)

