import re
from datetime import datetime

from view.info import start_date_time, end_date_time


def id_validator(id_):
    return isinstance(id_, int) and id_ > 0


def passenger_validator(name):
    return isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name)

def location_validator(loc):
    return isinstance(loc, str) and len(loc) >= 2


def date_validator(_str):
    try:
        datetime.strptime(start_date_time, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def time_validator(time_str):
    try:
        datetime.strptime(end_date_time, "%H:%M")
        return True
    except ValueError:
        return False


def ticket_validator(ticket):
    errors = []
    if not id_validator(ticket.id):
        errors.append("Invalid ID")
    if not name_validator(ticket.name):
        errors.append("Invalid Name")
    if not location_validator(ticket.origin):
        errors.append("Invalid Origin")
    if not location_validator(ticket.destination):
        errors.append("Invalid Destination")
    if not date_validator(ticket.start_date_time):
        errors.append("Invalid Flight Date (yyyy-mm-dd)")
    if not time_validator(end_date_time):
        errors.append("Invalid Flight Time (hh:mm)")
    if not ticket_type_validator(ticket):
        errors.append("Invalid Ticket Type")
    return errors