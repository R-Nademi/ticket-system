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

def birth_date_validator(birth_date):
    if not (type(birth_date) == str and re.match(r"^\d{4}-\d{2}-\d{2}$",birth_date)):
        raise ValueError("Invalid birth date !!!")


def username_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z\s]{3,30}$",username)):
        raise ValueError("Invalid username !!!")


def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z\s]{3,30}$",password)):
        raise ValueError("Invalid password !!!")


def role_validator(role):
    if not (type(role) == str and re.match(r"^[a-zA-Z\s]{3,30}$",role)):
        raise ValueError("Invalid role !!!")




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







