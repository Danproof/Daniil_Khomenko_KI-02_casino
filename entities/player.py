from .base_entity import  Entity


class Player(Entity):
    def __init__(self, id: int,
                       account_id: int,
                       balance_id: int,):
        self._id = id
        self._account_id = account_id
        self._balance_id = balance_id

    def __str__(self):
        return f'Player({self._id}, account_id = {self._account_id}, balance_id = {self._balance_id})'

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
    def id(self, id):
        self._id = id

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        self._account_id = account_id

    @property
    def balance_id(self):
        return self._balance_id

    @balance_id.setter
    def balance_id(self, balance_id):
        self._balance_id = balance_id