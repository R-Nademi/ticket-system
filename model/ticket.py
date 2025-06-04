from model.validator import *

class Ticket:

    # سازنده کلاس برای مقداردهی اولیه مشخصات بلیط
    def init(self, name, origin, destination, date, time, price):
        self.name = name              # نام مسافر
        self.origin = origin          # مبدا پرواز
        self.destination = destination  # مقصد پرواز
        self.date = date              # تاریخ پرواز
        self.time = time              # ساعت پرواز
        self.price = price            # قیمت بلیط

    # متد اعتبارسنجی با استفاده از تابع خارجی
    def validate(self):
        return ticket_validator(self)

    # تبدیل شی به یک تاپل برای نمایش در جدول
    def to_tuple(self):
        return (self.name, self.origin, self.destination, self.date, self.time, self.price) # noqa