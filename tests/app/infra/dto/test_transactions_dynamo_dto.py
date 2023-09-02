from decimal import Decimal
from src.app.entities.transactions import Transactions
from src.app.enums.transactions_type_enum import TRANSACTIONS_TYPE_ENUM
from src.app.infra.dto.transactions_dynamo_dto import TransactionsDynamoDto


class Test_TransactionDynamoDto:
  def test_from_entity(self):
    transaction = Transactions(TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693658529835.8687)
    transactions_dynamo_dto = TransactionsDynamoDto.from_entity(transaction)

    expected_transactions_dto  = TransactionsDynamoDto(
      TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693658529835.8687
    )

    assert transactions_dynamo_dto.type_transaction == expected_transactions_dto.type_transaction 
    assert transactions_dynamo_dto.value == expected_transactions_dto.value 
    assert transactions_dynamo_dto.current_balance == expected_transactions_dto.current_balance 
    assert transactions_dynamo_dto.timestamp == expected_transactions_dto.timestamp 

  def test_to_dynamo(self):
    transactions_dto  = TransactionsDynamoDto(
    TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693658529835.8687
    )
      
    item = transactions_dto.to_dynamo()

    expected = {
        "type_transaction": "DEPOSIT",
        'entity': 'transactions',
        "value": Decimal('100.00'),
        "current_balance": Decimal('1100.00'),
        "timestamp": Decimal('1693658529835.8687'),
      }

    expected == item

  def test_from_entity_to_dynamo(self):
    transaction = Transactions(TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693658529835.8687)
    transactions_dynamo_dto = TransactionsDynamoDto.from_entity(transaction)

    item = transactions_dynamo_dto.to_dynamo()

    expected = {
        "type_transaction": "DEPOSIT",
        'entity': 'transactions',
        "value": Decimal('100.00'),
        "current_balance": Decimal('1100.00'),
        "timestamp": Decimal('1693658529835.8687'),
      }

    expected == item

  def test_from_dynamo(self):
    item = {'PK': 'transactions',
            'SK': 'transactions#1693661431284.0298',
            'current_balance': Decimal('1100'),
            'entity': 'transactions',
            'timestamp': Decimal('1693661431284.0298'),
            'type_transaction': 'DEPOSIT',
            'value': Decimal('100')}
    
    transactions_dto = TransactionsDynamoDto.from_dynamo(item)
    expected = TransactionsDynamoDto(
      TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693661431284.0298
    )

    assert transactions_dto.type_transaction == expected.type_transaction
    assert transactions_dto.value == expected.value
    assert transactions_dto.current_balance == expected.current_balance
    assert transactions_dto.timestamp == expected.timestamp

  def test_to_entity(self):
    transactions_dto = TransactionsDynamoDto(
      TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693661431284.0298
    )

    transactions = transactions_dto.to_entity()

    expected = Transactions(
      TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693661431284.0298
    )

    assert transactions.type_transaction == expected.type_transaction
    assert transactions.value == expected.value
    assert transactions.current_balance == expected.current_balance
    assert transactions.timestamp == expected.timestamp
  
  def test_from_dynamo_to_entity(self):
    item = {'PK': 'transactions',
            'SK': 'transactions#1693661431284.0298',
            'current_balance': Decimal('1100'),
            'entity': 'transactions',
            'timestamp': Decimal('1693661431284.0298'),
            'type_transaction': 'DEPOSIT',
            'value': Decimal('100')}
    
    transactions_dto = TransactionsDynamoDto.from_dynamo(item)

    transactions = transactions_dto.to_entity()

    expected = Transactions(
      TRANSACTIONS_TYPE_ENUM.DEPOSIT, 100.00, 1100.00, 1693661431284.0298
    )

    assert transactions.type_transaction == expected.type_transaction
    assert transactions.value == expected.value
    assert transactions.current_balance == expected.current_balance
    assert transactions.timestamp == expected.timestamp






    