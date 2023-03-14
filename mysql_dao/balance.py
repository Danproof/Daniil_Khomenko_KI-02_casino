from typing import List

from utils import singleton
from idao import BalanceIDAO
from entities import Balance
from .with_connection_meta import WithConnectionMeta


@singleton
class BalanceDAO(BalanceIDAO, metaclass=WithConnectionMeta):
    def select_all(self, cursor) -> List[Balance]:
        stmt = 'SELECT * FROM balance'
        cursor.execute(stmt)
        balances = [Balance(*row) for row in cursor.fetchall()]
        return balances

    def find_by_id(self, cursor, balance_id: int) -> Balance:
        stmt = f'SELECT * FROM balance WHERE id = %s'
        cursor.execute(stmt, (balance_id,))
        result = cursor.fetchall()
        if result:
            return Balance(*result[0])

    def insert(self, cursor, balances: List[Balance]):
        for balance in balances:
            stmt = f'INSERT INTO balance VALUES {balance.attributes}'
            cursor.execute(stmt)

    def update(self, cursor, balances: List[Balance]):
        stmt = 'UPDATE balance SET real_money = %s, ' + \
                                  'chips = %s, ' + \
                              'WHERE id = %s'
        for balance in balances:
            cursor.execute(stmt, (*balance.attributes[1:], balance.id))

    def delete(self, cursor, balances: List[Balance]):
        for balance in balances:
            stmt = f'DELETE FROM balance WHERE id = {balance.id}'
            cursor.execute(stmt)