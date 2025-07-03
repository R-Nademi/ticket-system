from model.tools.validator import *

class Ticket:
    def __init__(self,id_, name, origin, destination,start_date_time,end_date_time,ticket_type, price):
     self.id_ = id_
     self.name = name
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value


    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        origin_validator(value)
        self._origin = value