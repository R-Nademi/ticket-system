import  unittest
from model.file_manager import file_name
from model.ticket import Ticket
from datetime import datetime





t = Ticket("1", "Ali","Mohammad",
                   "Mashhad", "10:30",
           "14:00", "16:00", "Airline")


print("code test passed" if t.code == "1" else "code test failed")
print("name test passed" if t.name == "Ali" else "name test failed")
print("family test passed" if t.family == "Mohammad" else "family test failed")
print("origin test passed" if t.origin == "Mashhad" else "origin test failed")
print("destination test passed" if t.destination == "10:30" else "destination test failed")
print("start_date_time test passed" if t.start_date_time ==  "14:00" else "start_date_time test failed")
print("end_date_time test passed" if t.end_date_time == "16:00" else "end_date_time test failed")
print("ticket_type test passed" if t.ticket_type == "Airline" else "ticket_type test failed")
print("price test passed" if t.price == "economy" else "price test failed")


if file_name == 'mine':
    unittest.main()