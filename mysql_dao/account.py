from typing import List

from utils import *
from idao import AccountIDAO
from entities import Account
from .with_connection_meta import WithConnectionMeta


@singleton
class AccountDAO(AccountIDAO, metaclass=WithConnectionMeta):
    def select_all(self, cursor) -> List[Account]:
        stmt = 'SELECT * FROM account'
        cursor.execute(stmt)
        accounts = [Account(*row) for row in cursor.fetchall()]
        return accounts

    def find_by_username(self, cursor, username: str) -> Account:
        stmt = f'SELECT * FROM account WHERE username = %s'
        cursor.execute(stmt, (username,))
        result = cursor.fetchall()
        if result:
            return Account(*result[0])

    def insert(self, cursor, accounts: List[Account]):
        for account in accounts:
            stmt = f'INSERT INTO account VALUES {account.attributes}'
            cursor.execute(stmt)

    def update(self, cursor, accounts: List[Account]):
        stmt = 'UPDATE account SET username = %s, ' + \
                                  'password = %s, ' + \
                                  'first_name = %s, ' + \
                                  'last_name = %s, ' + \
                                  'email = %s ' + \
                              'WHERE id = %s'
        for account in accounts:
            print((*account.attributes[1:], account.id))
            cursor.execute(stmt, (*account.attributes[1:], account.id))

    def delete(self, cursor, accounts: List[Account]):
        for account in accounts:
            stmt = f'DELETE FROM account WHERE id = {account.id}'
            cursor.execute(stmt)
