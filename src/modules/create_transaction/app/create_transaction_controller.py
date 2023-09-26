from ....shared.domain.entities.transactions import Transactions
from ....shared.domain.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from ..app.create_transaction_usecase import CreateTransactionUseCase
from ..app.create_transaction_viewmodel import CreateTransactionViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError 

class CreateTransactionController:

    def __init__(self, usecase: CreateTransactionUseCase):
        self.CreateTransactionUseCase = usecase
    def __call__(self, request: dict) -> IResponse:
        try:
            lista_parametros = ["2","5","10","20","50","100","200","type"]
            for n in lista_parametros:
                if n not in request.keys():
                    raise MissingParameters(n)
            
            transaction = self.CreateTransactionUseCase(
                request=request,
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
        


            