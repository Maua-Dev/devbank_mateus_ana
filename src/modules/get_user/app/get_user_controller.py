
from ....shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from ..app.get_user_usecase import GetUserUsecase
from ..app.get_user_viewmodel import GetUserViewModel

from ....shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from ....shared.helpers.errors.domain_errors import EntityError
from ....shared.helpers.errors.usecase_errors import NoItemsFound
from ....shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError 



class GetUserController:
    def __init__(self, usecase: GetUserUsecase):
        self.usecase = usecase
    
    def __call__(self) -> IResponse:
        try:
            user = self.usecase()
            
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
            return InternalServerError(err)