
from enum import Enum
import os

from ..shared.domain.repositories.user_repository_interface import IUserRepository

from ..shared.helpers.errors.environment_errors import EnvironmentNotFound

from ..shared.domain.repositories.transactions_repository_interface import ITransactionsRepository



class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_transaction_repo() -> ITransactionsRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from ..shared.infra.repositories.transactions_repository_mock import TransactionsRepositoryMock
            return TransactionsRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from ..shared.infra.repositories.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return self.__dict__