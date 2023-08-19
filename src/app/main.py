from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

# from .repo.transactions_repository_mock import TransactionsRepositoryMock

# from .repo.user_repository_mock import UserRepositoryMock

# from .errors.entity_errors import ParamNotValidated

# from .enums.transactions_type_enum import TransactionsTypeEnum

# from .entities.transactions import Transactions




app = FastAPI()

userRepo = Environments.get_user_repo()()

transactionRepo = Environments.get_transaction_repo()()

@app.get("/")

def get_user():
     user = userRepo.get_user()

     return user.to_dict()

@app.get("/history")

def get_all_transactions():
     transactions = transactionRepo.get_all_transactions()

     transaction_list = [transaction.to_dict() for transaction in transactions]
     return {
          'transaction':transaction_list
     }

     





    


handler = Mangum(app, lifespan="off")
