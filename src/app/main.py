from fastapi import FastAPI
from mangum import Mangum

from ..shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from .environments import Environments


from ..modules.get_all_transactions.app.get_all_transactions_usecase import GetAllTransactionsUseCase
from ..modules.get_all_transactions.app.get_all_transactions_controller import GetAllTransactionsController
from ..modules.create_transaction.app.create_transaction_usecase import CreateTransactionUseCase
from ..modules.create_transaction.app.create_transaction_controller import CreateTransactionController
from ..modules.get_user.app.get_user_usecase import GetUserUsecase
from ..modules.get_user.app.get_user_controller import GetUserController



app = FastAPI()

user_repo = Environments.get_user_repo()()

transaction_repo = Environments.get_transaction_repo()()


@app.get("/")
def get_user():
     usecase = GetUserUsecase(user_repo)
     controller = GetUserController(usecase)
     return controller()

@app.get("/history")
def get_all_transactions():
     usecase = GetAllTransactionsUseCase(transaction_repo)
     controller = GetAllTransactionsController(usecase)
     return controller()

@app.post("/deposit")
def deposit(request: dict):
     request["type"] = TRANSACTIONS_TYPE_ENUM.DEPOSIT
     usecase = CreateTransactionUseCase(transaction_repo, user_repo)
     controller = CreateTransactionController(usecase)
     transaction = controller(request)
     return transaction

     
@app.post("/withdraw")
def withdraw(request: dict):
     request["type"] = TRANSACTIONS_TYPE_ENUM.WITHDRAW
     usecase = CreateTransactionUseCase(transaction_repo, user_repo)
     controller = CreateTransactionController(usecase)
     transaction = controller(request)
     return transaction




    


handler = Mangum(app, lifespan="off")
