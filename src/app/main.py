from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.transacoes_repository_mock import ItemRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.item_type_enum import ItemTypeEnum

from .entities.transacoes import Item


app = FastAPI()

repo = Environments.get_item_repo()()


    


handler = Mangum(app, lifespan="off")
