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
            dict_request = {"type": "", "value": "", "current_balance": "" , "timestamp": ""}
            for r in dict_request.keys():
                value = request.data.get(r)
                if value is None:
                    raise MissingParameters(r)
                dict_request[r] = value
            transaction = self.CreateTransactionUseCase(
                type_transaction=dict_request['type'],
                value=dict_request['value'],
                current_balance=dict_request['current_balance'],
                timestamp=dict_request['timestamp'],
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
        


            