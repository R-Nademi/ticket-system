import re
from datetime import datetime




def code_validator(code):
    if not (type(code) == str and re.match(r"^[a-zA_Z\s]{3,30}$",code)):
        raise ValueError("Invalid code !!!")


def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name)):
        raise ValueError("Invalid name !!!")

def family_validator(family):
    if not (type(family) == str and re.match(r"^[a-zA-Z\s]{3,30}$",family)):
        raise ValueError("Invalid family !!!")


def origin_validator(origin):
    if not (type(origin) == str and re.match(r"^[a-zA-Z\s]{3,30}$", origin)):
        raise ValueError("Invalid origin !!!")


def destination_validator(destination):
    if not (type(destination) == str and re.match(r"^[a-zA-Z\s]{3,30}$",destination)):
        raise ValueError("Invalid destination !!!")


def start_date_time_validator(start_date_time):
    if not (type(start_date_time) == str and re.match(r"^[a-zA-Z\s]{3,30}$",start_date_time)):
        raise ValueError("Invalid start_date_time !!!")




def end_date_time_validator(end_date_time):
    if not (type(end_date_time) == str and re.match(r"^[a-zA-Z\s]{3,30}$",end_date_time)):
        raise ValueError("Invalid end_date_time !!!")



def ticket_type_validator(ticket_type):
    if not (type(ticket_type)== str and re.match(r"^[a-zA-Z\s]{3,30}$", ticket_type)):
        raise ValueError("Invalid ticket_type !!!")



def price_validator(price):
    if not (type(price) == str and re.match(r"^[a-zA-Z\s]{3,30}$", price)):
        raise ValueError("Invalid price !!!")




def ticket_validator(ticket):
    errors = []
    if not code_validator(ticket.code):
        errors.append("Code")
    if not name_validator(ticket.name):
        errors.append("Name")
    if not family_validator(ticket.family):
        errors.append("Family")
    if not origin_validator(ticket.origin):
        errors.append("Origin")
    if not destination_validator(ticket.destination):
        errors.append("Destination")
    if not start_date_time_validator(ticket.start_date_time):
        errors.append("Start_date_time_")
    if not end_date_time_validator(ticket.end_date_time):
        errors.append("End_date_time")
    if not ticket_type_validator(ticket.ticket_type):
        errors.append("Ticket_Type")
    if not price_validator(ticket.price):
        errors.append("Price")
    return errors