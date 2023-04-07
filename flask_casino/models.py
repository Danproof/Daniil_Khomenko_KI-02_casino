from factories import *
from flask_casino import login_manager


dbms = 'mysql'

pool = PoolFactory.get_pool(dbms)
pool.connect()


# User table
dao_user = DAO_Factory.get_dao(dbms).get_dao_implementation('user')


@login_manager.user_loader
def load_user(user_id):
    return dao_user.find_by_id(user_id)