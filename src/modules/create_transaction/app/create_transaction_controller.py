from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .create_transaction_usecase import CreateTransactionUseCase
from .create_transaction_viewmodel import CreateTransactionViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError 

class CreateTransactionController:

    def __init__(self, usecase: CreateTransactionUseCase):
        self.CreateTransactionUseCase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            lista_notas = ["2","5","10","20","50","100","200"]
            if type(request.data.get("type")) is None:
                raise WrongTypeParameter("type")
            for n in lista_notas:
                if n not in request.data.get("request").keys():
                    raise MissingParameters("Request must be a dict with keys 2,5,10,20,50,100,200")
            
            
            transaction = self.CreateTransactionUseCase(
                type=request.data.get("type"),
                request=request.data.get("request")
            )
            viewmodel = CreateTransactionViewModel(transaction)

            return OK(viewmodel.to_dict())
        
        except NoItemsFound as err:
            return NotFound(body=err.message)
        
        except MissingParameters as err:
            return BadRequest(body=err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(body=err.message)
        
        except EntityError as err:
            return BadRequest(body=err.message)
        
        except Exception as err:
            return InternalServerError(body=err)
        


            