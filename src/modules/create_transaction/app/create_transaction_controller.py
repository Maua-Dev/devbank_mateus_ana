from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .create_transaction_usecase import CreateTransactionUseCase
from .create_transaction_viewmodel import CreateTransactionViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import NotFound, BadRequest, InternalServerError 

class CreateTransactionController:

    def __init__(self, usecase: CreateTransactionUseCase):
        self.CreateTransactionUseCase = usecase
    def __call__(self, request: IRequest) -> IResponse:
        try:
            list_request = []
            for r in request:
                if request.data.get(r) is None:
                    raise MissingParameters(r)
                list_request.append(r)
            
            transaction = self.CreateTransactionUseCase(
                name=list_request[0],
                agency=list_request[1],
                account=list_request[2],
                current_balance=list_request[3]
            )

            viewmodel = CreateTransactionViewModel(transaction)

            return viewmodel.to_dict()
        
        except NoItemsFound as err:
            return NotFound(err.message)
        
        except MissingParameters as err:
            return BadRequest(err.message)
        
        except WrongTypeParameter as err:
            return BadRequest(err.message)
        
        except EntityError as err:
            return BadRequest(err.message)
        
        except Exception as err:
            return InternalServerError(err.message)
        


            