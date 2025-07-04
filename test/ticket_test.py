
from model.entity.ticket import Ticket






ticket = Ticket(1, "Ali", "AliPour",
                   "Mashhad", "10:30",
           "14:00", "16:00", "Airline")

print(ticket)
print(ticket.to_tuple())