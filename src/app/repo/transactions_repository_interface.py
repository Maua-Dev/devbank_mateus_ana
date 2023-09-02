from abc import ABC, abstractmethod
from typing import List

from ..entities.transactions import Transactions


class IITransactionsRepository(ABC):

    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass
    """
    Get a List of transactions

    Parameters
    --------------------
    self: self

    Returns
    --------------------
    List[Objects]
        a list of objects of the class Transaction
    """

    @abstractmethod
    def create_transaction(self, transaction: Transactions) -> Transactions:
        pass

    """
    create object transaction

    Parameters
    -------------------------
    self : self

    transaction: Class(Transactions)
    
    Returns
    ---------------------------
    Object
        transactions

        ex:
        Transactions(
          type_transaction= TRANSACTIONS_TYPE_ENUM.DEPOSIT.value,
          value=float(total_value),
          current_balance=total_value + user["current_balance"],
          timestamp = time.time()*1000
     )    

    """


        
        