from .base_entity import Entity


class Account(Entity):
    def __init__(self, id: int,
                       username: str,
                       password: str,
                       first_name: str,
                       last_name: str,
                       email: str,):
        self._id = id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    def __str__(self):
        return f'Account{self._id, self._username, self.password, self._first_name, self._last_name,  self._email,}'

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, Account):
            return self._id == other._id
        return NotImplemented

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._username = password

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email