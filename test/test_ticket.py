import unittest

from model.file_manager import file_name # noqa
from model.ticket import Ticket

class TestTicket(unittest.TestCase):
    def test_create_ticket(self):
        t = Ticket("Ali", "Tehran", "Mashhad", # noqa
                   "2025-06-10", "10:30", "14:00", "A23", "Economy", "123456") # noqa

        self.assertEqual(t.name, "Ali")
        self.assertEqual(t.origin, "Tehran")
        self.assertEqual(t.destination, "Mashhad")
        self.assertEqual(t.date, "2025-06-10")
        self.assertEqual(t.departure_time, "10:30") # noqa
        self.assertEqual(t.arrival_time, "14:00") # noqa
        self.assertEqual(t.seat, "A23") # noqa
        self.assertEqual(t.class_type, "Economy") # noqa
        self.assertEqual(t.ticket_number, "123456") # noqa

if file_name == 'mine':
    unittest.main()