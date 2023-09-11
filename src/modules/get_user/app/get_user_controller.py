
from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .get_user_usecase import GetUserUsecase
from .get_user_viewmodel import GetUserViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError 



class GetUserController:
    def __init__(self, usecase: GetUserUsecase):
        self.usecase = usecase
    
    def __call__(self, request: IRequest) -> IResponse:
        try:
            user = self.usecase(
                name=request.data.get('name'),
                agency=request.data.get('agency'),
                account=request.data.get('account'),
                current_balance=request.data.get('current_balance')
            )
            
            viewmodel = GetUserViewModel(user)

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