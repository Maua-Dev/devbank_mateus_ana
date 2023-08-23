from abc import ABC, abstractmethod
from typing import List

from ..entities.transactions import Transactions


class IITransactionsRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass
    """Method: Function get_all_transactions  return a list of all the transactions that the user made in the account"""


    def create_transaction(self, transaction: Transactions) -> Transactions:
        pass

    """Method: Function create_transaction receives the class Transactions and return an object of Transactions
    with the Parameters(type_transaction, value,current_balance,timestamp)"""
    

        
        