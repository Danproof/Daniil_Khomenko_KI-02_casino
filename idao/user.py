from abc import ABC, abstractmethod
from typing import List

from entities.user import User


class UserIDAO(ABC):
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
    def insert(self, cursor,  users: List[User]):
        '''
        Should insert given list of users
        '''

    @abstractmethod
    def update(self, cursor,  users: List[User]):
        '''
        Should update given list of users
        '''

    @abstractmethod
    def delete(self, cursor,  users: List[User]):
        '''
        Should delete given list of users and
        '''