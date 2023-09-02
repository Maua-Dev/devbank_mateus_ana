
from enum import Enum
import os

from .repo.user_repository_interface import IUserRepository

from .errors.environment_errors import EnvironmentNotFound

from .repo.transactions_repository_interface import IITransactionsRepository


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

        if self.stage == STAGE.TEST:
            self.s3_bucket_name = "bucket-test"
            self.region = "sa-east-1"
            self.endpoint_url = "http://localhost:8000"
            self.dynamo_table_name = "soller-capacitacao-0209-table"
            self.dynamo_partition_key = "PK"
            self.dynamo_sort_key = "SK"
            self.cloud_front_distribution_domain = "https://d3q9q9q9q9q9q9.cloudfront.net"

        else:
            self.s3_bucket_name = os.environ.get("S3_BUCKET_NAME")
            self.region = os.environ.get("REGION")
            self.endpoint_url = os.environ.get("ENDPOINT_URL")
            self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")
            self.dynamo_partition_key = os.environ.get("DYNAMO_PARTITION_KEY")
            self.dynamo_sort_key = os.environ.get("DYNAMO_SORT_KEY")
            self.cloud_front_distribution_domain = os.environ.get(
                "CLOUD_FRONT_DISTRIBUTION_DOMAIN")

    @staticmethod
    def get_transaction_repo() -> IITransactionsRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transactions_repository_mock import TransactionsRepositoryMock
            return TransactionsRepositoryMock
        elif Environments.get_envs().stage in [STAGE.DEV, STAGE.PROD]:
            from .repo.transactions_repository_dynamo import TransactionsRepositoryDynamo
            return TransactionsRepositoryDynamo
        else:
            raise EnvironmentNotFound("STAGE")

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage in [STAGE.TEST, STAGE.DEV, STAGE.PROD]:
            from .repo.user_repository_mock import UserRepositoryMock
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
