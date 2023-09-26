from typing import List

from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from ....shared.domain.entities.transactions import Transactions
from ..app.get_all_transactions_usecase import GetAllTransactionsUseCase
from ..app.get_all_transactions_viewmodel import GetAllTransactionsViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError 


class GetAllTransactionsController:
    def __init__(self, usecase: GetAllTransactionsUseCase):
        self.usecase = usecase
    
    def __call__(self) -> IResponse:
        try:
            all_transactions: List[Transactions] = self.usecase()

            viewmodel = GetAllTransactionsViewModel(all_transactions)
            return OK(viewmodel.to_dict())
        
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
