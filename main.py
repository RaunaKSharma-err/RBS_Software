from tkinter import *

root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap("icon.ico")
headingLabel = Label(
    root,
    text="Retail Billing System",
    font=("times new roman", 30, "bold"),
    bg="gray20",
    fg="gold",
    bd=12,
    relief="groove",
)
headingLabel.pack(fill=X)

customer_details_frames = LabelFrame(
    root,
    text="Customer Details",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="gold",
    bd=8,
    relief="groove",
)
customer_details_frames.pack(fill=X)

name_label = Label(
    customer_details_frames,
    text="Name",
    font=("times new roman", 15),
    bg="gray20",
    fg="white",
    padx=10,
)
name_label.grid(row=0, column=0)

name_entry = Entry(customer_details_frames, font=("arial", 12), width=15)
name_entry.grid(row=0, column=1, pady=10)

PhoneNumber_label = Label(
    customer_details_frames,
    text="Phone Number",
    font=("times new roman", 15),
    bg="gray20",
    fg="white",
    padx=10,
)
PhoneNumber_label.grid(row=0, column=2)

PhoneNumber_entry = Entry(customer_details_frames, font=("arial", 12), width=15)
PhoneNumber_entry.grid(row=0, column=3, pady=10)

Bill_label = Label(
    customer_details_frames,
    text="Bill Number",
    font=("times new roman", 15),
    bg="gray20",
    fg="white",
    padx=10,
)
Bill_label.grid(row=0, column=4)

Bill_entry = Entry(customer_details_frames, font=("arial", 12), width=15)
Bill_entry.grid(row=0, column=5, pady=10)


root.mainloop()
