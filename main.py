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
customer_details_frames.pack(fill=X, pady=5)

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
    font=("times new roman", 13, "bold"),
    bd=5,
    width=15,
)
Search_Button.grid(row=0, column=6, pady=5, padx=20)

productFrame = Frame(root)
productFrame.pack()

cosmetics_product_frames = LabelFrame(
    productFrame,
    text="Cosmetics",
    font=("times new roman", 15, "bold"),
    bd=8,
    bg="gray20",
    fg="gold",
    relief=GROOVE,
    width=20,
)
cosmetics_product_frames.grid(row=0, column=0, padx=5)

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
    productFrame,
    text="Grocery",
    font=("times new roman", 15, "bold"),
    bd=8,
    bg="gray20",
    fg="gold",
    relief=GROOVE,
    width=20,
)
grocery_frames.grid(row=0, column=1)

rice = Label(
    grocery_frames,
    text="Rice",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
rice.grid(row=0, column=0)

rice_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
rice_entry.grid(row=0, column=1, padx=20)

oil = Label(
    grocery_frames,
    text="Oil",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
oil.grid(row=1, column=0)

oil_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
oil_entry.grid(row=1, column=1)

Daal = Label(
    grocery_frames,
    text="Daal",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Daal.grid(row=2, column=0)

Daal_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Daal_entry.grid(row=2, column=1)

Wheat = Label(
    grocery_frames,
    text="Wheat",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Wheat.grid(row=3, column=0)

Wheat_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Wheat_entry.grid(row=3, column=1)

Sugar = Label(
    grocery_frames,
    text="Sugar",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Sugar.grid(row=4, column=0)

Sugar_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Sugar_entry.grid(row=4, column=1)

Tea = Label(
    grocery_frames,
    text="Tea",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Tea.grid(row=5, column=0)

Tea_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Tea_entry.grid(row=5, column=1)

# Cold drinks frames

grocery_frames = LabelFrame(
    productFrame,
    text="Cold Drinks",
    font=("times new roman", 15, "bold"),
    bd=8,
    bg="gray20",
    fg="gold",
    relief=GROOVE,
    width=20,
)
grocery_frames.grid(row=0, column=2, padx=5)

Mazza = Label(
    grocery_frames,
    text="Mazza",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Mazza.grid(row=0, column=0)

Mazza_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Mazza_entry.grid(row=0, column=1, padx=20)

Pepsi = Label(
    grocery_frames,
    text="Pepsi",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Pepsi.grid(row=1, column=0)

Pepsi_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Pepsi_entry.grid(row=1, column=1)

Sprite = Label(
    grocery_frames,
    text="Sprite",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Sprite.grid(row=2, column=0)

Sprite_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Sprite_entry.grid(row=2, column=1)

Dew = Label(
    grocery_frames,
    text="Dew",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Dew.grid(row=3, column=0)

Dew_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Dew_entry.grid(row=3, column=1)

Frooti = Label(
    grocery_frames,
    text="Frooti",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
Frooti.grid(row=4, column=0)

Frooti_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
Frooti_entry.grid(row=4, column=1)

CocaCola = Label(
    grocery_frames,
    text="Coca Cola",
    font=("times new roman", 14),
    fg="white",
    bg="gray20",
    pady=10,
    padx=20,
)
CocaCola.grid(row=5, column=0)

CocaCola_entry = Entry(grocery_frames, font=("arial", 15), width=8, bd=5)
CocaCola_entry.grid(row=5, column=1)

BillFrame = Frame(productFrame, bd=8, relief=GROOVE)
BillFrame.grid(row=0, column=3)

Bill_label = Label(
    BillFrame, text="Bill", font=("times new roman", 15, "bold"), relief=GROOVE, padx=5
)
Bill_label.pack(fill=X)

scrollbar = Scrollbar(BillFrame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(BillFrame, width=49, height=16, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)


root.mainloop()
