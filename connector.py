from abc import ABCMeta, abstractmethod
from mysql.connector import pooling, Error

from utils import singleton


db_config = {
    'user': 'root',
    'password': '1111',
    'host': '127.0.0.1',
    'database': 'casino',
    'pool_name': 'mypool',
    'pool_size': 3
}

class Pool(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        '''
        Should connect using connection pool
        '''

    @abstractmethod
    def get_connection(self):
        '''
        Should return connetion
        '''

    @abstractmethod
    def close(self):
        '''
        Should close all connections from pool
        '''


@singleton
class MySQLPool(Pool):
    def connect(self):
        try:
            self.pool = pooling.MySQLConnectionPool(**db_config)
        except Error as e:
            print(f'Error while setting up connection pool: {e}')
            exit('pool')

    def get_connection(self):
        try:
            return self.pool.get_connection()
        except Error as e:
            print(f'Error connecting to database: {e}')
            exit('connection')

    def close(self):
        self.pool._remove_connections()