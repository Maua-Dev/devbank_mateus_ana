from typing import List

from ..infra.dto.transactions_dynamo_dto import TransactionsDynamoDto

from ..environments import Environments

from ..infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource

from ..entities.transactions import Transactions
from ..repo.transactions_repository_interface import IITransactionsRepository

from boto3.dynamodb.conditions import Key


class TransactionsRepositoryDynamo(IITransactionsRepository):

    @staticmethod
    def partition_key_format() -> str:
        return f"transactions"

    @staticmethod
    def sort_key_format(timestamp: float) -> str:
        return f"transactions#{timestamp}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_all_transactions(self) -> List[Transactions]:
        query_string = Key(self.dynamo.partition_key).eq(self.partition_key_format())
        resp = self.dynamo.query(key_condition_expression=query_string, Select='ALL_ATTRIBUTES')
        
        if resp.get('Items') is None:
            return []
        
        transactions_list = []
        for item in resp.get('Items'):
            transactions_list.append(TransactionsDynamoDto.from_dynamo(item).to_entity())


        return transactions_list


    def create_transaction(self, transaction: Transactions) -> Transactions:
        transactions_dto = TransactionsDynamoDto.from_entity(transaction)

        item = transactions_dto.to_dynamo()

        resp = self.dynamo.put_item(partition_key=self.partition_key_format(),
                                    sort_key=self.sort_key_format(transaction.timestamp), item=item,
                                    is_decimal=True)

        return transaction