from idlelib.query import CustomRun

from model.entity.ticket import Ticket


ticket_list = []

class usercontroller:
    def save(self,code,name,family,username,password,role):
        try:
            ticket = Ticket(code,name,family,username,password,role)
            ticket_list.append(ticket)
            return True,f"ticket save successfully{ticket}"
        except Exception as e:
            return False,f"save error{e}"

    def edit(self,code,name, family,username,password,role):
        try:
            ticket = Ticket(code,name,family,username,password,role)
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
            return False, f"ticket find all failed\n{e}"


    def sell(self):
        try:
            return True, f"ticket sell successfully - {ticket_list}"
        except Exception as e:
            return False, f"ticket sell failed\n{e}"


    def role(self):
        try:
            for user in ticket_list:
                if user.role == "admin":
                    return True, f"ticket admin successfully - {user}"

            else:
                 return False, f"ticket customer "
