from decimal import Decimal

import boto3
import dotenv
from src.app.repo.transactions_repository_dynamo import TransactionsRepositoryDynamo

from src.app.repo.transactions_repository_mock import TransactionsRepositoryMock


def setup_dynamo_table():
    dynamo_table_name = "soller-capacitacao-0209-table"
    endpoint_url = "http://localhost:8000"
    print("Setting up DynamoDB table...")

    dynamo_client = boto3.client('dynamodb', endpoint_url=endpoint_url)
    print("DynamoDB client created")
    tables = dynamo_client.list_tables()['TableNames']

    if dynamo_table_name not in tables:
        print("Creating table...")
        dynamo_client.create_table(
            TableName=dynamo_table_name,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                }

            ],
            BillingMode='PAY_PER_REQUEST',
        )
        print("Waiting for table to be created...")
        dynamo_client.get_waiter('table_exists').wait(
            TableName=dynamo_table_name)

        print('Loading table...')

        print('Table "soller-capacitacao-0209-table" created!')

    else:
        print("Table already exists!")


def load_mock_to_local_dynamo():
    repo_mock = TransactionsRepositoryMock()
    repo_dynamo = TransactionsRepositoryDynamo()

    count = 0

    print('Loading mock data to dynamo...')
    for transactions in repo_mock.transactions:
        print(
            f"Loading transaction {transactions.type_transaction} | {transactions.value} | {transactions.current_balance} | {transactions.timestamp} ")
        repo_dynamo.create_transaction(transactions)
        count += 1

    print(f"{count} transaction loaded to dynamo!")


if __name__ == '__main__':
    # setup_dynamo_table()
    load_mock_to_local_dynamo()
