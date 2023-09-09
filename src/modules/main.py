import time
from fastapi import FastAPI, HTTPException
from mangum import Mangum


from .entities.transactions import Transactions
from .enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM

from .environments import Environments





app = FastAPI()

user_repo = Environments.get_user_repo()()

transaction_repo = Environments.get_transaction_repo()()

@app.get("/")

def get_user():
     user = user_repo.get_user()
     return user.to_dict()

@app.get("/history")

def get_all_transactions():
     transactions = transaction_repo.get_all_transactions()

     transaction_list = [transaction.to_dict() for transaction in transactions]
     return {
          'all_transactions':transaction_list
     }

@app.post("/deposit")

def deposit(request: dict):
     if request.keys() != {"2","5","10","20","50","100","200"}:
          raise HTTPException(status_code=400, detail="Invalid deposit!")
     
     user = user_repo.get_user().to_dict()
     total_value = sum([int(k)*v for k,v in request.items()])

     if total_value > 2*user["current_balance"]:
          raise HTTPException(status_code=403, detail="Suspicious transaction")
     if total_value <= 0:
          raise HTTPException(status_code=400, detail="Total deposit must be positive")
     
     transaction = Transactions(
          type_transaction= TRANSACTIONS_TYPE_ENUM.DEPOSIT,
          value=float(total_value),
          current_balance=total_value + user["current_balance"],
          timestamp = time.time()*1000
     )    


     transaction_repo.create_transaction(transaction)
     user_repo.deposit_current_balance(total_value)

     return transaction.to_dict()

     
@app.post("/withdraw")

def withdraw(request: dict):
     if request.keys() != {"2","5","10","20","50","100","200"}:
          raise HTTPException(status_code=400, detail="Invalid withdraw!")

     user = user_repo.get_user().to_dict()
     total_value = sum([int(k)*v for k,v in request.items()])
     if total_value > user["current_balance"]:
          raise HTTPException(status_code=403, detail="Insufficient balance for transaction")

     transaction = Transactions(
          type_transaction =  TRANSACTIONS_TYPE_ENUM.WITHDRAW,
          value=float(total_value),
          current_balance= user["current_balance"] - total_value,
          timestamp=time.time()*1000
     )

     transaction_repo.create_transaction(transaction)
     user_repo.withdraw_current_balance(total_value)

     return transaction.to_dict()



    


handler = Mangum(app, lifespan="off")