from importlib import import_module

from dbms_validation import validate
from connector import *


class DBMS_DAO_Factory:
    def __init__(self, dbms: str):
        self.dbms_dao = import_module(f'{dbms}_dao')

    def get_dao_implementation(self, option: str):
        m_dao = {
            'user': self.dbms_dao.UserDAO,
            'player': self.dbms_dao.PlayerDAO,
            'balance': self.dbms_dao.BalanceDAO,
                 }
        if option.lower() in m_dao:
            return m_dao[option.lower()]()


class DAO_Factory:
    @staticmethod
    def get_dao(dbms: str):
        validate(dbms)
        return DBMS_DAO_Factory(dbms)


class PoolFactory:
    @staticmethod
    def get_pool(dbms: str) -> Pool:
        validate(dbms)
        dbms_pool = {
            'mysql': MySQLPool
            }
        return dbms_pool[dbms]()


