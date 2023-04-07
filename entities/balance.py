from .base_entity import Entity


class Balance(Entity):
    def __init__(self, balance_id: int,
                       real_money: float = 0,
                       chips: int = 0,):
        self._id = balance_id
        self._real_money = real_money
        self._chips = chips

    def __str__(self):
        return f'Balance({self._id}, real_money = {self._real_money}, chips = {self._chips})'

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Balance):
            return self._id == other._id
        return NotImplemented

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, balance_id):
        self._id = balance_id

    @property
    def real_money(self):
        return self._real_money

    @real_money.setter
    def real_money(self, real_money):
        self._real_money = real_money

    @property
    def chips(self):
        return self._chips

    @chips.setter
    def chips(self, chips):
        self._chips = chips
