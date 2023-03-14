from functools import wraps
from abc import ABC

from connector import MySQLPool


def with_connection(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        pool = MySQLPool()
        conn = pool.get_connection()
        with conn.cursor() as cursor:
            result = method(self, cursor, *args, **kwargs)
        conn.commit()
        conn.close()
        return result
    return wrapper


class WithConnectionMeta(type(ABC), type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                dct[attr_name] = with_connection(attr_value)
        return super().__new__(cls, name, bases, dct)