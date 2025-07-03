from model.tools.validator import *


class User:
    def __init__(self, code, name, family, username,password,):
        self.code = code
        self.name = name
        self.family = family


    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(self.__dict__.values())


    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        code__Validator(code)
        self._code = code