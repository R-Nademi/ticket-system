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


    def delete(self,code):
        try:
            return true, f"ticket removed successfully - {code}"
        except Exception as e:
            return false, f"ticket removed failed\n{e}"



    def find_all(self):
        try:
            return True,ticket_list
        except Exception as e:
            return False,f"find error{e}"


