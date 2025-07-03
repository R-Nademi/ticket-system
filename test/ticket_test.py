from model.repository.file_manager import file_name
from model.entity.ticket import Ticket
from datetime import datetime





ticket = Ticket(1, "Ali", "Mohammad",
                   "Mashhad", "10:30",
           "14:00", "16:00", "Airline")

print(ticket)
print(ticket.to_tuple())