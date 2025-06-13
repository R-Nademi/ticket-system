import re # noqa
from datetime import datetime


def id_validator(id): # noqa
    return isinstance(id, int) and id > 0


def passenger_validator(name):
    return isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name)

def location_validator(loc):
    return isinstance(loc, str) and len(loc) >= 2


def date_validator(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def time_validator(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def ticket_validator(ticket):
    errors = []
    if not id_validator(ticket.id):
        errors.append("Invalid ID")
    if not passenger_validator(ticket.passenger_name):
        errors.append("Invalid Passenger Name")
    if not location_validator(ticket.origin):
        errors.append("Invalid Origin")
    if not location_validator(ticket.destination):
        errors.append("Invalid Destination")
    if not date_validator(ticket.flight_date):
        errors.append("Invalid Flight Date (yyyy-mm-dd)")
    if not time_validator(ticket.flight_time):
        errors.append("Invalid Flight Time (hh:mm)")
    return errors