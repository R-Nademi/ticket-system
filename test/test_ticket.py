from model.file_manager import file_name
from model.ticket import Ticket
from model.ticket_type import ticket_type


t = Ticket("Ali", "Tehran", "Mashhad",
                   "2025-06-10", "10:30", "14:00", "airline", "Economy")




if file_name == 'mine':
    ticket_type.main()