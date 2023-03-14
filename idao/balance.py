from abc import ABC, abstractmethod
from typing import List

from entities.balance import Balance


class BalanceIDAO(ABC):
    @abstractmethod
    def select_all(self, cursor):
        '''
        Should return list of balances
        '''

    @abstractmethod
    def find_by_id(self, cursor,  balance_id: str):
        '''
        Should return balance with given id
        or None if no such balance found
        '''

    @abstractmethod
    def insert(self, cursor,  balances: List[Balance]):
        '''
        Should insert given list of balances
        '''

    @abstractmethod
    def update(self, cursor,  balances: List[Balance]):
        '''
        Should update given list of balances
        '''

    @abstractmethod
    def delete(self, cursor,  balances: List[Balance]):
        '''
        Should delete given list of balances
        '''