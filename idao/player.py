from abc import ABC, abstractmethod
from typing import List

from entities.player import Player



class PlayerIDAO(ABC):
    @abstractmethod
    def select_all(self, cursor):
        '''
        Should return list of players
        '''

    @abstractmethod
    def find_by_id(self, cursor,  player_id: str):
        '''
        Should return player with given id
        or None if no such player found
        '''

    @abstractmethod
    def insert(self, cursor,  players: List[Player]):
        '''
        Should insert given list of players
        '''

    @abstractmethod
    def update(self, cursor,  players: List[Player]):
        '''
        Should update given list of players
        '''

    @abstractmethod
    def delete(self, cursor,  players: List[Player]):
        '''
        Should delete given list of players
        '''