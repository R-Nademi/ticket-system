from model.validator import *

class Ticket:

    # سازنده کلاس برای مقداردهی اولیه مشخصات بلیط
    def __init__(self ,id_, name, origin, destination,start_date_time,end_date_time,airline, price):
        self.id_ = id_
        self.name = name
        self.origin = origin
        self.destination = destination
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.airline = airline
        self.price = price

    # متد اعتبارسنجی با استفاده از تابع خارجی
    def validate(self):
        return ticket_validator(self)

    # تبدیل شی به یک تاپل برای نمایش در جدول
    def to_tuple(self):
        return (self.id_,self.name, self.origin, self.destination, self.start_date_time,
                self.end_date_time, self.airline, self.price)