from entities import *
from factories import *


dbms = 'mysql'


def main():
    pool = PoolFactory.get_pool(dbms)
    pool.connect()

    # User table
    dao_user = DAO_Factory.get_dao(dbms).get_dao_implementation('user')

    # insert
    user1 = User(1, 'new_user_1', '1111', 'F1', 'L1', 'new_user1@gmail.com')
    user2 = User(2, 'new_user_2', '2222', 'F2', 'L2', 'new_user2@gmail.com')
    dao_user.insert([user1, user2])

    # select all
    users = dao_user.select_all()
    print('Select all', *users, '\n\n', sep='\n')

    # find by username
    user1 = dao_user.find_by_username('new_user_1')
    print('Find by username\n', user1, '\n\n')

    # update
    user2 = dao_user.find_by_username(user2.username)
    user2.username = 'Danproof'
    dao_user.update([user2])

    # select all
    users = dao_user.select_all()
    print('Select all', *users, '\n\n', sep='\n')

    # delete
    dao_user.delete([user1, user2])

    pool.close()
