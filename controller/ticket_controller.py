from model.entity.ticket import Ticket


ticket_list = []

class ticketcontroller:
    def save(self,code,name,family,birth_date,origin,destination,start_date_time,end_date_time,ticket_type,price):
        try:
            ticket = Ticket(code,name,family,birth_date,origin,destination,start_date_time,end_date_time,ticket_type,price)
            ticket_list.append(ticket)
            return True,f"ticket save successfully{ticket}"
        except Exception as e:
            return False,f"save error{e}"


    def edit(self,code,name, family,birth_date,origin,destination,start_date_time,end_date_time,ticket_type,price):
        try:
            ticket = Ticket(code,name,family,birth_date,origin,destination,start_date_time,end_date_time,ticket_type,price)
            return True,f"ticket edit successfully{ticket}"
        except Exception as e:
            return False,f"edit error{e}"



    def remove(self,code):
        try:
            return True, f"ticket removed successfully - {code}"
        except Exception as e:
            return False, f"ticket removed failed\n{e}"



    def find_all(self):
        try:
            return True, f"ticket find all successfully - {ticket_list}"
        except Exception as e:
            return False,f"ticket find all failed\n{e}"


    def sell(self):
        try:
            return True, f"ticket sell successfully - {ticket_list}"
        except Exception as e:
            return False,f"ticket sell failed\n{e}"



