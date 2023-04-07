from typing import List

from utils import *
from idao import UserIDAO
from entities import User
from .with_connection_meta import WithConnectionMeta


@singleton
class UserDAO(UserIDAO, metaclass=WithConnectionMeta):
    def select_all(self, cursor) -> List[User]:
        stmt = 'SELECT * FROM user'
        cursor.execute(stmt)
        users = [User(*row) for row in cursor.fetchall()]
        return users

    def find_by_id(self, cursor, user_id: int) -> User:
        stmt = f'SELECT * FROM user WHERE id = %s'
        cursor.execute(stmt, (user_id,))
        result = cursor.fetchall()
        if result:
            return User(*result[0])

    def find_by_username(self, cursor, username: str) -> User:
        stmt = f'SELECT * FROM user WHERE username = %s'
        cursor.execute(stmt, (username,))
        result = cursor.fetchall()
        if result:
            return User(*result[0])

    def find_by_email(self, cursor, email: str) -> User:
        stmt = f'SELECT * FROM user WHERE email = %s'
        cursor.execute(stmt, (email,))
        result = cursor.fetchall()
        if result:
            return User(*result[0])

    def insert(self, cursor, users: List[User]):
        for user in users:
            stmt = f'INSERT INTO user VALUES {user.attributes}'
            cursor.execute(stmt)

    def update(self, cursor, users: List[User]):
        stmt = 'UPDATE user SET username = %s, ' + \
                                  'password = %s, ' + \
                                  'first_name = %s, ' + \
                                  'last_name = %s, ' + \
                                  'username = %s ' + \
                              'WHERE id = %s'
        for user in users:
            print((*user.attributes[1:], user.id))
            cursor.execute(stmt, (*user.attributes[1:], user.id))

    def delete(self, cursor, users: List[User]):
        for user in users:
            stmt = f'DELETE FROM user WHERE id = {user.id}'
            cursor.execute(stmt)
