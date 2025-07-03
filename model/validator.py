import re
from datetime import datetime




def codevalidator(code):
    return isinstance(code, int) and code > 0


def name_validator(name):
    return isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", name)

def origin_validator(origin):
    return isinstance(origin, str) and re.match(r"^[a-zA-Z\s]{3,30}$", origin)

def destination_validator(destination):
    return isinstance(destination, str) and len(destination) >= 10


def start_date_time_validator(time):
    try:
        from view.info import start_date_time, end_date_time
        datetime.strptime(start_date_time, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def end_date_time_validator(time):
    try:
        from view.info import start_date_time, end_date_time
        datetime.strptime(end_date_time,"%Y-%m-%d")
        return True
    except ValueError:
        return False


def ticket_type_validator(ticket_type):
    return isinstance(ticket_type, str) and re.match(r"^[a-zA-Z\s]{3,30}$", ticket_type)



def price_validator(price):
    return isinstance(price, str) and re.match(r"^[a-zA-Z\s]{3,30}$", price)




def ticket_validator(ticket):
    errors = []
    if not codevalidator(ticket.id):
        errors.append("code")
    if not name_validator(ticket.name):
        errors.append("Name")
    if not origin_validator(ticket.origin):
        errors.append("origin")
    if not destination_validator(ticket.destination):
        errors.append("Destination")
    if not start_date_time_validator(ticket.start_date_time):
        errors.append("start_date_time_")
    if not end_date_time_validator(ticket.end_date_time):
        errors.append("end_date_time")
    if not ticket_type_validator(ticket.ticket_type):
        errors.append("Ticket_Type")
    if not price_validator(ticket.price):
        errors.append("Price")
    return errors