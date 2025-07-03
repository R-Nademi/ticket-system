from model.entity.ticket import Ticket
from test.ticket_test import ticket

ticket_list = []

class TicketController:
    def save(self,code,name,family,origin,destination,start_date_time,end_date_time,ticket_type,price):
        try:
            ticket = Ticket(code,name,family,origin,destination,start_date_time,end_date_time,ticket_type,price)
            ticket_list.append(ticket)
            return True,f"ticket save successfully{ticket}"
        except Exception as e:
            return False,f"save error{e}"

    def edit(self,code,name, family,origin,destination,start_date_time,end_date_time,ticket_type):
        try:
            ticket = Ticket(code,name,family,origin,destination,start_date_time,end_date_time,ticket_type)
            return True,f"ticket edit successfully{ticket}"
        except Exception as e:
            return False,f"edit error{e}"

    def find_all(self):
        try:
            return True,ticket_list
        except Exception as e:
            return False,f"find error{e}"

