from model.validator import *


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


    def validate(self):
        return ticket_validator(self)


    def to_tuple(self):
        return (self.id_,self.name, self.origin, self.destination, self.start_date_time,self.end_date_time,self.ticket_type, self.price) # noqa