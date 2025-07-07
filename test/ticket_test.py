from model.entity.ticket import Ticket


ticket = Ticket(1, "Ali", "AliPour",
                   "1360", "Mashhad",
           "Tehran", "10.30", "12.00")


print(ticket)
print(ticket.to_tuple())