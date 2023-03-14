from abc import ABC, abstractmethod
from typing import List

from entities.account import Account


class AccountIDAO(ABC):
    @abstractmethod
    def select_all(self, cursor):
        '''
        Should return list of users
        '''

    @abstractmethod
    def find_by_username(self, cursor,  username: str):
        '''
        Should return user with given username
        or None if no such user found
        '''

    @abstractmethod
    def insert(self, cursor,  accounts: List[Account]):
        '''
        Should insert given list of users
        '''

    @abstractmethod
    def update(self, cursor,  accounts: List[Account]):
        '''
        Should update given list of users
        '''

    @abstractmethod
    def delete(self, cursor,  accounts: List[Account]):
        '''
        Should delete given list of users and
        '''