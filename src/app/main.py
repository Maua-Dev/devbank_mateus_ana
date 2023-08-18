from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.transactions_repository_mock import TransactionsRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.transactions_type_enum import TransactionsTypeEnum

from .entities.transactions import Transactions




app = FastAPI()

repo = Environments.get_item_repo()()


    


handler = Mangum(app, lifespan="off")
