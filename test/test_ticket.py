from model.file_manager import file_name
from model.ticket import Ticket
from datetime import datetime

t = Ticket(
    "Ali","Tehran","Mashhad",2023,12,15,20,0,2023,12,15,21,0, "Economy", "IranAir", "123456")


print("name test passed" if t.name == "Ali" else "name test failed")
print("origin test passed" if t.origin == "Tehran" else "origin test failed")
print("destination test passed" if t.destination == "Mashhad" else "destination test failed")
print("date time test passed" if t.date == "2021-12-15" else "date time test failed")
print("date time test passed" if t.date == "2021-12-15" else "date time test failed")
print("economy test passed" if t.date == "2021-12-15 hour:20" else "economy test failed")
print("economy test passed" if t.date == "2021-12-15 hour:21" else "economy test failed")
















