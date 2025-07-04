from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.repository.file_manager import *
from model.entity.ticket import Ticket
from model.entity.ticket import datetime
from view.info import family



def load_data():
    global ticket_list
    ticket_list = read_from_file()



    for ticket in ticket_list:
        table.insert("", END, values=ticket.to_tuple())


def reset_form():
    code.set("")
    name.set("")
    origin.set("")
    destination.set("")
    start_date_time.set("")
    end_date_time.set("")
    ticket_type.set("")
    price.set("")
    load_data()


def save_btn_click():
    ticket = Ticket(code.get(), name.get(),family.get(), origin.get(), destination.get(),
                    start_date_time.get(),end_date_time.get(), ticket_type.get(), int(price.get()))
    errors = ticket.values()
    if errors:
        msg.showerror("Error", "\n".join(errors))
    else:
        msg.showinfo("Success", "Ticket saved successfully.")
        ticket_list.append(ticket)
        write_to_file(ticket_list)
        reset_form()


def table_select(event):
    print(event.widget.get()
    selected = table.item(table.focus())["values"]
    if selected:
        selected_ticket = Ticket(*selected)
        code.set(selected_ticket.code)
        name.set(selected_ticket.name)
        family.set(selected_ticket.family)
        origin.set(selected_ticket.origin)
        destination.set(selected_ticket.destination)
        start_date_time.set(selected_ticket.start_date_time)
        end_date_time.set(selected_ticket.end_date_time)
        ticket_type.set(selected_ticket.ticket_type)
        price.set(selected_ticket.price)


def edit_btn_click():
    selected_index = None
    for i, ticket in enumerate(ticket_list):
        if ticket.name == name.get() and ticket.start_date_time == start_date_time.get():
            selected_index = i
            break

    if selected_index is not None:
        updated = Ticket(code.get(),name.get(), origin.get(), destination.get(),start_date_time.get(),end_date_time.get(),
                         ticket_type.get(), int(price.get()))
        errors = updated.values()
        if errors:
            msg.showerror("Error", "\n".join(errors))
        else:
            ticket_list[selected_index] = updated
            write_to_file(ticket_list) # noqa
            reset_form()
            msg.showinfo("Success", "Ticket updated successfully.")
    else:
        msg.showerror("Error", "Ticket not found for editing.")

# حذف بلیط
def remove_btn_click():
    target_name = name.get()
    target_date = start_date_time.get()
    for i, ticket in enumerate(ticket_list):
        if ticket.name == target_name and ticket.date_time == target_date:
            if msg.askyesno("Confirm", "Are you sure to delete this ticket?"):
                del ticket_list[i]
                write_to_file(ticket_list) # noqa
                reset_form()
                msg.showinfo("Deleted", "Ticket deleted successfully.")
                return
    msg.showerror("Error", "Ticket not found or not selected.")

# -------------------- طراحی رابط گرافیکی --------------------

# ایجاد پنجره اصلی
window = Tk()
window.title("Ticket Info")
window.geometry("1100x400")

# تعریف متغیرهای فرم
code = StringVar()
name = StringVar()
origin = StringVar()
destination = StringVar()
start_date_time = StringVar()
end_date_time = StringVar()
ticket_type = StringVar()
price = StringVar()

# ساخت لیبل‌ها و ورودی‌ها در سمت چپ با متد place
Label(window, text="code:").place(x=20,y=20)
Entry(window, textvariable=code).place(x=130,y=20)

Label(window, text="name:").place(x=20, y=20)
Entry(window, textvariable=name).place(x=130, y=20)

Label(window, text="origin:").place(x=20, y=60)
Entry(window, textvariable=origin).place(x=130, y=60)

Label(window, text="destination:").place(x=20, y=100)
Entry(window, textvariable=destination).place(x=130, y=100)

Label(window, text="start_date_time:").place(x=20, y=140)
Entry(window, textvariable=start_date_time).place(x=130, y=140)

Label(window, text="end_date_time:").place(x=20, y=180)
Entry(window, textvariable=end_date_time).place(x=130, y=180)

Label(window, text="ticket_type:").place(x=20, y=20)
Entry(window, textvariable=ticket_type).place(x=130, y=20)

Label(window, text="Price:").place(x=20, y=220)
Entry(window, textvariable=price).place(x=130, y=220)

# جدول سمت راست برای نمایش بلیط‌ها
table = ttk.Treeview(window, columns=("code","name", "origin", "destination", "start_date_time","end_date_time","ticket_type","price"), show="headings")
table.heading("code", text="code")
table.heading("name", text="name")
table.heading("origin", text="origin")
table.heading("destination", text="destination")
table.heading("start_date_time", text="start_date_time")
table.heading("end_date_time", text="end_date_time")
table.heading("ticket_type", text="ticket_type")
table.heading("price", text="Price")

# تنظیم عرض ستون‌ها
table.column("code", width=50)
table.column("name", width=100)
table.column("origin", width=100)
table.column("destination", width=100)
table.column("start_date_time", width=120)
table.column("end_date_time", width=120)
table.column("ticket_type", width=80)
table.column("price", width=80)

# جایگذاری جدول در سمت راست
table.place(x=320, y=20, height=350)
table.bind("<<TreeviewSelect>>", table_select)

# دکمه‌ها پایین فرم
Button(window, text="Save", width=10, command=save_btn_click).place(x=20, y=280)
Button(window, text="Edit", width=10, command=edit_btn_click).place(x=130, y=280)
Button(window, text="Remove", width=10, command=remove_btn_click).place(x=20, y=320)
Button(window, text="Clear", width=10, command=reset_form).place(x=130, y=320)

# بارگذاری اولیه داده‌ها از فایل
load_data()

# اجرای حلقه اصلی برنامه
window.mainloop()