from .base_entity import Entity


class Player(Entity):
    def __init__(self, player_id: int,
                       user_id: int,
                       balance_id: int,):
        self._id = player_id
        self._user_id = user_id
        self._balance_id = balance_id

    def __str__(self):
        return f'Player({self._id}, user_id = {self._user_id}, balance_id = {self._balance_id})'

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Player):
            return self._id == other._id
        return NotImplemented

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, player_id):
        self._id = player_id

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def balance_id(self):
        return self._balance_id

    @balance_id.setter
    def balance_id(self, balance_id):
        self._balance_id = balance_id
