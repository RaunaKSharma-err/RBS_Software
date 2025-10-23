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
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    padx=10,
)
name_label.grid(row=0, column=0, padx=15)

name_entry = Entry(customer_details_frames, font=("arial", 12), width=15, bd=5)
name_entry.grid(row=0, column=1, pady=10, padx=15)

PhoneNumber_label = Label(
    customer_details_frames,
    text="Phone Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    padx=10,
)
PhoneNumber_label.grid(row=0, column=2, padx=15)

PhoneNumber_entry = Entry(customer_details_frames, font=("arial", 12), width=15, bd=5)
PhoneNumber_entry.grid(row=0, column=3, pady=10, padx=15)

Bill_label = Label(
    customer_details_frames,
    text="Bill Number",
    font=("times new roman", 15, "bold"),
    bg="gray20",
    fg="white",
    padx=10,
)
Bill_label.grid(row=0, column=4, padx=15)

Bill_entry = Entry(customer_details_frames, font=("arial", 12), width=15, bd=5)
Bill_entry.grid(row=0, column=5, pady=10, padx=15)

Search_Button = Button(
    customer_details_frames,
    text="Search",
    font=("times new roman", 15, "bold"),
    bd=5,
    width=15,
)
Search_Button.grid(row=0, column=6, pady=10, padx=20)

productFrame = Frame(root)
productFrame.pack()

cosmetics_product_frames = LabelFrame(
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    bd=8,
    bg="gray20",
    fg="gold",
    relief=GROOVE,
    width=20,
)
cosmetics_product_frames.grid(row=0, column=0)

bath_soap = Label(
    cosmetics_product_frames,
    text="Bath Soap",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
bath_soap.grid(row=0, column=0)

bath_soap_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
bath_soap_entry.grid(row=0, column=1, padx=20)

face_cream = Label(
    cosmetics_product_frames,
    text="Face Cream",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
face_cream.grid(row=1, column=0)

face_cream_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
face_cream_entry.grid(row=1, column=1)

face_wash = Label(
    cosmetics_product_frames,
    text="Face Wash",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
face_wash.grid(row=2, column=0)

face_wash_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
face_wash_entry.grid(row=2, column=1)

hair_spray = Label(
    cosmetics_product_frames,
    text="Hair Spray",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
hair_spray.grid(row=3, column=0)

hair_spray_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
hair_spray_entry.grid(row=3, column=1)

Hair_gel = Label(
    cosmetics_product_frames,
    text="Hair Gel",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Hair_gel.grid(row=4, column=0)

Hair_gel_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
Hair_gel_entry.grid(row=4, column=1)

body_lotion = Label(
    cosmetics_product_frames,
    text="Body Lotion",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
body_lotion.grid(row=5, column=0)

body_lotion_entry = Entry(cosmetics_product_frames, font=("arial", 15), width=8, bd=5)
body_lotion_entry.grid(row=5, column=1)

# grocery customer_details_frames

grocery_frames = LabelFrame(
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    bd=8,
    bg="gray20",
    fg="gold",
    relief=GROOVE,
    width=20,
)
grocery_frames.grid(row=0, column=1)

bath_soap = Label(
    grocery_frames,
    text="Bath Soap",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
bath_soap.grid(row=0, column=0)

bath_soap_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
bath_soap_entry.grid(row=0, column=1, padx=20)

face_cream = Label(
    grocery_frames,
    text="Face Cream",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
face_cream.grid(row=1, column=0)

face_cream_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
face_cream_entry.grid(row=1, column=1)

face_wash = Label(
    grocery_frames,
    text="Face Wash",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
face_wash.grid(row=2, column=0)

face_wash_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
face_wash_entry.grid(row=2, column=1)

hair_spray = Label(
    grocery_frames,
    text="Hair Spray",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
hair_spray.grid(row=3, column=0)

hair_spray_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
hair_spray_entry.grid(row=3, column=1)

Hair_gel = Label(
    grocery_frames,
    text="Hair Gel",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Hair_gel.grid(row=4, column=0)

Hair_gel_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Hair_gel_entry.grid(row=4, column=1)

body_lotion = Label(
    grocery_frames,
    text="Body Lotion",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
body_lotion.grid(row=5, column=0)

body_lotion_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
body_lotion_entry.grid(row=5, column=1)


root.mainloop()
