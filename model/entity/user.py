from model.tools.validator import *


class Ticket:
    def __init__(self, code, name, family, origin, destination, start_date_time, end_date_time, ticket_type, price):
        self.code = code
        self.name = name
        self.family = family
        self.origin = origin
        self.destination = destination
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.ticket_type = ticket_type
        self.price = price

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