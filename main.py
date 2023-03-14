from entities import *
from factories import *


dbms = 'mysql'


def main():
    pool = PoolFactory.get_pool(dbms)
    pool.connect()

    # Account table
    dao_account = DAO_Factory.get_dao(dbms).get_dao_implementation('account')

    # insert
    account1 = Account(1, 'new_user_1', '1111', 'F1', 'L1', 'new_user1@gmail.com')
    account2 = Account(2, 'new_user_2', '2222', 'F2', 'L2', 'new_user2@gmail.com')
    dao_account.insert([account1, account2])

    # select all
    accounts = dao_account.select_all()
    print('Select all', *accounts, '\n\n', sep='\n')

    # find by username
    account1 = dao_account.find_by_username('new_user_1')
    print('Find by username\n', account1, '\n\n')

    # update
    account2 = dao_account.find_by_username(account2.username)
    account2.username = 'Danproof'
    dao_account.update([account2])

    # select all
    accounts = dao_account.select_all()
    print('Select all', *accounts, '\n\n', sep='\n')

    # delete
    dao_account.delete([account1, account2])

    pool.close()


if __name__ == '__main__':
    main()
