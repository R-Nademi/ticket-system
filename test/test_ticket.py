from model.file_manager import file_name  # noqa
from model.ticket import Ticket
from datetime import datetime

t = Ticket(
    "Ali",
    "Tehran",
    "Mashhad",
    datetime(2023, 12, 15, 20, 0),
    datetime(2023, 12, 15, 21, 0),
    "Economy",
    "IranAir"
    "123456")  # noqa

print("Name Test Passed" if t.name == "Ali" else "Name Test Failed")
print("Origin Test Passed" if t.origin == "Tehran" else "Origin Test Failed")

# self.assertEqual(t.origin, "Tehran")
# self.assertEqual(t.destination, "Mashhad")
# self.assertEqual(t.date, "2025-06-10")
# self.assertEqual(t.departure_time, "10:30") # noqa
# self.assertEqual(t.arrival_time, "14:00") # noqa
# self.assertEqual(t.seat, "A23") # noqa
# self.assertEqual(t.class_type, "Economy") # noqa
# self.assertEqual(t.ticket_number, "123456") # noqa
