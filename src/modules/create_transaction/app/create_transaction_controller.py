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
            if request.data.get("type") is None:
                raise MissingParameters("type")
            if request.data.get("value") is None:
                raise MissingParameters("value")
            if request.data.get("current_balance") is None:
                raise MissingParameters("current_balance")
            if request.data.get("timestamp") is None:
                raise MissingParameters("timestamp")
            transaction = self.CreateTransactionUseCase(
                type_transaction=request.data.get("type") ,
                value=request.data.get("value"),
                current_balance=request.data.get("current_balance"),
                timestamp=request.data.get("timestamp"),
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
            print(err)
            return InternalServerError(body=err)
        


            