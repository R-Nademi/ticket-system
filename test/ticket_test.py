from model.repository.file_manager import file_name
from model.entity.ticket import Ticket
from datetime import datetime





ticket = Ticket(1, "Ali", "Mashad",
                   "2025-06-10", "10:30",
           "14:00", "airline", "Economy")

print(ticket)
print(ticket.to_tuple())