from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.file_manager import *  # noqa
from model.ticket import Ticket

# لیست کلی بلیط‌ها (در حافظه نگهداری می‌شود)
ticket_list = []

# تابع بارگذاری اطلاعات از فایل و نمایش در جدول
def load_data():
    global ticket_list
    ticket_list = read_from_file() # noqa # خواندن داده‌ها از فایل

    # پاک‌سازی جدول
    for row in table.get():
        table.delete(row)

    # اضافه‌کردن بلیط‌ها به جدول
    for ticket in ticket_list:
        table.insert("", END, values=ticket.to_tuple())

# پاک‌سازی فرم
def reset_form():
    name.set("")
    origin.set("")
    destination.set("")
    date.set("")
    time.set("")
    price.set("")
    load_data()  # بازخوانی جدول

# ذخیره‌سازی بلیط جدید
def save_btn_click():
    ticket = Ticket( name.get(), origin.get(), destination.get(), # noqa
                    date.get(), time.get(), int(price.get())) # noqa
    errors = ticket.validate()
    if errors:
        msg.showerror("Error", "\n".join(errors))
    else:
        msg.showinfo("Success", "Ticket saved successfully.")
        ticket_list.append(ticket)
        write_to_file(ticket_list) # noqa
        reset_form()

# انتخاب بلیط از جدول
def table_select(event):
    print(event.widget.get())
    selected = table.item(table.focus())["values"]
    if selected:
        selected_ticket = Ticket(*selected) # noqa
        name.set(selected_ticket.name)
        origin.set(selected_ticket.origin)
        destination.set(selected_ticket.destination)
        date.set(selected_ticket.date)
        time.set(selected_ticket.time)
        price.set(selected_ticket.price)

# ویرایش بلیط
def edit_btn_click():
    selected_index = None
    for i, ticket in enumerate(ticket_list):
        if ticket.name == name.get() and ticket.date == date.get():
            selected_index = i
            break

    if selected_index is not None:
        updated = Ticket(name.get(), origin.get(), destination.get(), # noqa
                         date.get(), time.get(), int(price.get())) # noqa
        errors = updated.validate()
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
    target_date = date.get()
    for i, ticket in enumerate(ticket_list):
        if ticket.name == target_name and ticket.date == target_date:
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
window.geometry("900x400")  # عرض بیشتر برای جدول سمت راست

# تعریف متغیرهای فرم
id_ = StringVar()
name = StringVar()
origin = StringVar()
destination = StringVar()
start_date_time = StringVar()
end_date_time = StringVar()
airline = StringVar()
price = StringVar()

# ساخت لیبل‌ها و ورودی‌ها در سمت چپ با متد place
Label(window, text="Passenger Name:").place(x=20, y=20)
Entry(window, textvariable=name).place(x=130, y=20)

Label(window, text="Origin:").place(x=20, y=60)
Entry(window, textvariable=origin).place(x=130, y=60)

Label(window, text="Destination:").place(x=20, y=100)
Entry(window, textvariable=destination).place(x=130, y=100)

Label(window, text="Date (YYYY-MM-DD):").place(x=20, y=140)
Entry(window, textvariable=date).place(x=130, y=140)

Label(window, text="Time (HH:MM):").place(x=20, y=180)
Entry(window, textvariable=time).place(x=130, y=180)

Label(window, text="Price:").place(x=20, y=220)
Entry(window, textvariable=price).place(x=130, y=220)

# جدول سمت راست برای نمایش بلیط‌ها
table = ttk.Treeview(window, columns=("name", "origin", "destination", "date", "time", "price"), show="headings")
table.heading("name", text="Name")
table.heading("origin", text="Origin")
table.heading("destination", text="Destination")
table.heading("date", text="Date")
table.heading("time", text="Time")
table.heading("price", text="Price")

# تنظیم عرض ستون‌ها
table.column("name", width=100)
table.column("origin", width=100)
table.column("destination", width=100)
table.column("date", width=100)
table.column("time", width=80)
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