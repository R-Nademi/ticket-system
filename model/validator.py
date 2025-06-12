import re # noqa
from datetime import datetime

from view.info import price


def id_validator(id_): # noqa
    return isinstance(id_, int) and id_ > 0


def passenger_validator(name):
    return isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name)

def location_validator(loc):
    return isinstance(loc, str) and len(loc) >= 2


def date_validator(star_date_time):
    try:
        datetime.strptime(star_date_time, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def time_validator(end_date_time):
    try:
        datetime.strptime(end_date_time, "%H:%M")
        return True
    except ValueError:
        return False


def ticket_validator(ticket):
    errors = []
    if not id_validator(ticket.id):
        errors.append("id_")
    if not passenger_validator(ticket.name):
        errors.append("name")
    if not location_validator(ticket.origin):
        errors.append("Origin")
    if not location_validator(ticket.destination):
        errors.append("Destination")
    if not date_validator(ticket.start_date_time):
        errors.append("start_date_time (yyyy-mm-dd)")
    if not time_validator(ticket.end_date_time):
        errors.append("end_date_time (hh:mm)")
    if not airline.validate(ticket.airline):
        errors.append("airline")
    if not price.validate(ticket.price):
        errors.append("Price")
    return errors