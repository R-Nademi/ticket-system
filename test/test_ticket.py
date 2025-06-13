from model.file_manager import file_name
from model.ticket import Ticket
from datetime import datetime

from view.info import end_date_time

t = Ticket("Ali", "Tehran", "Mashhad",
                   "2025-06-10", "10:30",
           "14:00", "airline", "Economy")


print("id_ test passed" if t.id_ == "ali" else "id_ test failed")
print("name test passed" if t.name == "tehran" else "name test failed")
print("origin test passed" if t.origin == "mashhad" else "origin test failed")
print("destination test passed" if t.destination == "2025-06-10" else "destination test failed")
print("start_date_time test passed" if t.start_date_time ==  "10:30" else "start_date_time test failed")
print("end_date_time test passed" if t.end_date_time == "14:00" else "end_date_time test failed")
print("ticket_type test passed" if t.ticket_type == "airline" else "ticket_type test failed")
print("price test passed" if t.price == "economy" else "price test failed")


if file_name == 'mine':
    datetime.main()