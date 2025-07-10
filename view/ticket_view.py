from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.ticket_controller import TicketController
from model.repository.file_manager import *
from model.entity.ticket import Ticket


class TicketView:
    def load_data(self):
        global ticket_list
        ticket_list = read_from_file()

        for ticket in ticket_list:
            self.table.insert("", END, values=ticket.to_tuple())

    def reset_form(self):
        self.code.set("")
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.origin.set("")
        self.destination.set("")
        self.start_date_time.set("")
        self.end_date_time.set("")
        self.ticket_type.set("")
        self.seat_number.set("")
        self.price.set(0)

        self.load_data()

    def save_btn_click(self):
        ticket_controller = TicketController()
        errors = ticket_controller.save(self.code.get(), self.name.get(), self.family.get(), self.birth_date.get(), self.origin.get(), self.destination.get(),
                        self.start_date_time.get(), self.end_date_time.get(), self.ticket_type.get(), self.seat_number.get(),
                        self.price.get())
        if errors:
            msg.showerror("Error", "\n".join(errors))
        else:
            msg.showinfo("Success", "Ticket saved successfully.")
            # ticket_list.append(ticket)
            # write_to_file(ticket_list)
            self.reset_form()

    def table_select(self,event):
        print(event.widget.get())
        selected = self.table.item(self.table.focus())["values"]
        if selected:
            selected_ticket = Ticket(*selected)
            self.code.set(selected_ticket.code)
            self.name.set(selected_ticket.name)
            self.family.set(selected_ticket.family)
            self.birth_date.set(selected_ticket.birth_date)
            self.origin.set(selected_ticket.origin)
            self.destination.set(selected_ticket.destination)
            self.start_date_time.set(selected_ticket.start_date_time)
            self.end_date_time.set(selected_ticket.end_date_time)
            self.ticket_type.set(selected_ticket.ticket_type)
            self.seat_number.set(selected_ticket.seat_number)
            self.price.set(selected_ticket.price)

    def edit_btn_click(self):
        selected_index = None
        for i, ticket in enumerate(ticket_list):
            if ticket.name == self.name.get() and ticket.start_date_time == self.start_date_time.get():
                selected_index = i
                break

        if selected_index is not None:
            updated = Ticket(self.code.get(), self.name.get(), self.family.get(), self.birth_date.get(), self.origin.get(), self.destination.get(),
                             self.start_date_time.get(), self.end_date_time.get(),
                             self.ticket_type.get(), self.seat_number.get(), int(self.price.get()))
            errors = updated.values()
            if errors:
                msg.showerror("Error", "\n".join(errors))
            else:
                ticket_list[selected_index] = updated
                write_to_file(ticket_list)  # noqa
                self.reset_form()
                msg.showinfo("Success", "Ticket updated successfully.")
        else:
            msg.showerror("Error", "Ticket not found for editing.")

    # حذف بلیط
    def remove_btn_click(self):
        target_name = self.name.get()
        target_date = self.start_date_time.get()
        for i, ticket in enumerate(ticket_list):
            if ticket.name == target_name and ticket.date_time == target_date:
                if msg.askyesno("Confirm", "Are you sure to delete this ticket?"):
                    del ticket_list[i]
                    write_to_file(ticket_list)  # noqa
                    self.reset_form()
                    msg.showinfo("Deleted", "Ticket deleted successfully.")
                    return
        msg.showerror("Error", "Ticket not found or not selected.")

    # -------------------- طراحی رابط گرافیکی --------------------

    def __init__(self):
        # ایجاد پنجره اصلی
        self.window = Tk()
        self.window.title("Ticket Info")
        self.window.geometry("1260x400")

        # تعریف متغیرهای فرم
        self.code = StringVar()
        self.name = StringVar()
        self.family = StringVar()
        self.birth_date = StringVar()
        self.origin = StringVar()
        self.destination = StringVar()
        self.start_date_time = StringVar()
        self.end_date_time = StringVar()
        self.ticket_type = StringVar()
        self.seat_number = StringVar()
        self.price = IntVar()

        # ساخت لیبل‌ها و ورودی‌ها در سمت چپ با متد place
        Label(self.window, text="code:").place(x=20, y=40)
        Entry(self.window, textvariable=self.code).place(x=130, y=40)

        Label(self.window, text="name:").place(x=20, y=60)
        Entry(self.window, textvariable=self.name).place(x=130, y=60)

        Label(self.window, text="family:").place(x=20, y=80)
        Entry(self.window, textvariable=self.family).place(x=130, y=80)

        Label(self.window, text="birth_date:").place(x=20, y=100)
        Entry(self.window, textvariable=self.birth_date).place(x=130, y=100)

        Label(self.window, text="origin:").place(x=20, y=140)
        Entry(self.window, textvariable=self.origin).place(x=130, y=140)

        Label(self.window, text="destination:").place(x=20, y=180)
        Entry(self.window, textvariable=self.destination).place(x=130, y=180)

        Label(self.window, text="start_date_time:").place(x=20, y=220)
        Entry(self.window, textvariable=self.start_date_time).place(x=130, y=220)

        Label(self.window, text="end_date_time:").place(x=20, y=240)
        Entry(self.window, textvariable=self.end_date_time).place(x=130, y=240)

        Label(self.window, text="Ticket Type").place(x=20, y=20)
        Entry(self.window, textvariable=self.ticket_type).place(x=130, y=20)

        Label(self.window, text="seat_number:").place(x=20, y=160)
        Entry(self.window, textvariable=self.seat_number).place(x=130, y=160)

        Label(self.window, text="Price:").place(x=20, y=200)
        Entry(self.window, textvariable=self.price).place(x=130, y=200)

        # جدول سمت راست برای نمایش بلیط‌ها
        self.table = ttk.Treeview(self.window, columns=("ticket_type", "code", "name", "family", "birth_date", "origin",
                                              "seat_number", "destination", "price", "start_date_time",
                                              "end_date_time"),
                             show="headings")
        self.table.heading("code", text="code")
        self.table.heading("name", text="name")
        self.table.heading("family", text="family")
        self.table.heading("birth_date", text="birth_date")
        self.table.heading("origin", text="origin")
        self.table.heading("destination", text="destination")
        self.table.heading("start_date_time", text="start_date_time")
        self.table.heading("end_date_time", text="end_date_time")
        self.table.heading("ticket_type", text="ticket_type")
        self.table.heading("seat_number", text="seat_number")
        self.table.heading("price", text="Price")

        # تنظیم عرض ستون‌ها
        self.table.column("code", width=50)
        self.table.column("name", width=80)
        self.table.column("family", width=95)
        self.table.column("birth_date", width=80)
        self.table.column("origin", width=95)
        self.table.column("destination", width=95)
        self.table.column("start_date_time", width=95)
        self.table.column("end_date_time", width=95)
        self.table.column("ticket_type", width=80)
        self.table.column("seat_number", width=80)
        self.table.column("price", width=80)

        # جایگذاری جدول در سمت راست
        self.table.place(x=320, y=20, height=350)
        self.table.bind("<<TreeviewSelect>>", self.table_select)

        # دکمه‌ها پایین فرم
        Button(self.window, text="Save", width=10, command=self.save_btn_click).place(x=20, y=280)
        Button(self.window, text="Edit", width=10, command=self.edit_btn_click).place(x=130, y=280)
        Button(self.window, text="Remove", width=10, command=self.remove_btn_click).place(x=20, y=320)
        Button(self.window, text="Clear", width=10, command=self.reset_form).place(x=130, y=320)
        Button(self.window, text="Search", width=10, command=self.reset_form).place(x=20, y=360)
        Button(self.window, text="Sell", width=10, command=self.reset_form).place(x=130, y=360)

        self.load_data()

        self.window.mainloop()