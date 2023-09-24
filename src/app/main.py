import time
from fastapi import FastAPI
from mangum import Mangum

from ..shared.domain.entities.transactions import Transactions
from ..shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from ..shared.environments import Environments

from ..shared.helpers.enum.http_status_code_enum import HttpStatusCodeEnum
from ..shared.helpers.external_interfaces.http_models import HttpRequest

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
     return controller().body

@app.get("/history")
def get_all_transactions():
     usecase = GetAllTransactionsUseCase(transaction_repo)
     controller = GetAllTransactionsController(usecase)

     
     return controller().body

@app.post("/deposit")
def deposit(request: dict):
     
     user = user_repo.get_user().to_dict()
     total_value = sum([int(k)*v for k,v in request.items()])
     total_value = float(total_value)
     
     request = HttpRequest(body={
          "type": TRANSACTIONS_TYPE_ENUM.DEPOSIT,
          "value": total_value,
          "current_balance": user["current_balance"] + total_value,
          "timestamp": time.time()*1000,
          "request": request
     })

     usecase = CreateTransactionUseCase(transaction_repo, user_repo)

     controller = CreateTransactionController(usecase)
     transaction = controller(request)
     return transaction

     
@app.post("/withdraw")
def withdraw(request: dict):

     
     user = user_repo.get_user().to_dict()
     total_value = sum([int(k)*v for k,v in request.items()])
     total_value = float(total_value)
     
     request = HttpRequest(body={
          "type": TRANSACTIONS_TYPE_ENUM.WITHDRAW,
          "value": total_value,
          "current_balance": user["current_balance"] - total_value,
          "timestamp": time.time()*1000,
          "request": request
     })

     usecase = CreateTransactionUseCase(transaction_repo, user_repo)

     controller = CreateTransactionController(usecase)
     transaction = controller(request)
     return transaction




    


handler = Mangum(app, lifespan="off")
