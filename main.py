from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 
from db import Database


 
db = Database("Employee.db")
root= Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="pink")
root.state("zoomed")


name=StringVar()
age=IntVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=IntVar()

# Entries Frame
entries_frame=Frame(root,bg="#535c68")
entries_frame.pack(side=TOP,fill=X)
title= Label(entries_frame,text="Employee Management System",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20, sticky="w")

#Labels
# Labels
lblname = Label(entries_frame, text="Name", font=("calibri", 16), bg="#535c68", fg="white")
lblname.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtname = Entry(entries_frame, textvariable=name, font=("calibri", 16))
txtname.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblage = Label(entries_frame, text="AGE", font=("calibri", 16), bg="#535c68", fg="white")
lblage.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtage = Entry(entries_frame, textvariable=age, font=("calibri", 16))
txtage.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.J", font=("calibri", 16), bg="#535c68", fg="white")
lbldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtdoj = Entry(entries_frame, textvariable=doj, font=("calibri", 16))
txtdoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblemail = Label(entries_frame, text="EMAIL", font=("calibri", 16), bg="#535c68", fg="white")
lblemail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtemail = Entry(entries_frame, textvariable=email, font=("calibri", 16))
txtemail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblgender = Label(entries_frame, text="GENDER", font=("calibri", 16), bg="#535c68", fg="white")
lblgender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
combogender=ttk.Combobox(entries_frame,font=("calibri", 16),textvariable=gender, state="readonly")
combogender['values'] = ("Male", "Female")
combogender.grid(row=3, column=1, padx=10, sticky="w")

lblcontact = Label(entries_frame, text="CONTACT NO", font=("calibri", 16), bg="#535c68", fg="white")
lblcontact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtcontact = Entry(entries_frame, textvariable=contact, font=("calibri", 16))
txtcontact.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lbladdress = Label(entries_frame, text="ADDRESS", font=("calibri", 16), bg="#535c68", fg="white")
lbladdress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtaddress = Text(entries_frame, width=75,height=5, font=("calibri", 16))
txtaddress.grid(row=5, column=0,columnspan=4, padx=10, sticky="w")

def getdata(event):
    select_row = tv.focus()
    data = tv.item(select_row)
    global row
    row = data["values"]

    if row and len(row) >= 8:
        name.set(row[1])
        age.set(row[2])
        doj.set(row[3])
        email.set(row[4])
        gender.set(row[5])
        contact.set(row[6])
        txtaddress.delete(1.0, END)
        txtaddress.insert(END, row[7])
    else:
        clearall()


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if (
        txtname.get() == ""
        or not txtage.get().isdigit()
        or not txtcontact.get().isdigit()
        or len(txtcontact.get()) < 10
        or txtdoj.get() == ""
        or txtemail.get() == ""
        or combogender.get() == ""
        or txtaddress.get(1.0, END) == ""
    ):
        error_message = "Please fill in all the details and provide a valid age, contact number (at least 10 digits), and other necessary information."
        if txtname.get() == "":
            error_message = "Please enter the name."
        elif not txtage.get().isdigit():
            error_message = "Please enter a valid age."
        elif not txtcontact.get().isdigit() or len(txtcontact.get()) < 10:
            error_message = "Please enter a valid contact number with at least 10 digits."
        elif txtdoj.get() == "":
            error_message = "Please enter the date of joining."
        elif txtemail.get() == "":
            error_message = "Please enter the email address."
        elif combogender.get() == "":
            error_message = "Please select the gender."
        elif txtaddress.get(1.0, END) == "":
            error_message = "Please enter the address."

        messagebox.showerror("Error in input", error_message)
        return
    db.insert(
        txtname.get(),
        txtage.get(),
        txtdoj.get(),
        txtemail.get(),
        combogender.get(),
        txtcontact.get(),
        txtaddress.get(1.0, END),
    )
    messagebox.showinfo("Success", "Record Inserted")
    clearall()
    displayAll()


def update_employee():
    if (
        txtname.get() == ""
        or not txtage.get().isdigit()
        or not txtcontact.get().isdigit()
        or len(txtcontact.get()) < 10
        or txtdoj.get() == ""
        or txtemail.get() == ""
        or combogender.get() == ""
        or txtcontact.get() == ""
        or txtaddress.get(1.0, END) == ""
    ):
        error_message = "Please fill in all the details and provide a valid age, contact number (at least 10 digits), and other necessary information."
        if txtname.get() == "":
            error_message = "Please enter the name."
        elif not txtage.get().isdigit():
            error_message = "Please enter a valid age."
        elif not txtcontact.get().isdigit() or len(txtcontact.get()) < 10:
            error_message = "Please enter a valid contact number with at least 10 digits."
        elif txtdoj.get() == "":
            error_message = "Please enter the date of joining."
        elif txtemail.get() == "":
            error_message = "Please enter the email address."
        elif combogender.get() == "":
            error_message = "Please select the gender."
        elif txtaddress.get(1.0, END) == "":
            error_message = "Please enter the address."

        messagebox.showerror("Error in input", error_message)
        return
    db.update(
        row[0],
        txtname.get(),
        txtage.get(),
        txtdoj.get(),
        txtemail.get(),
        combogender.get(),
        txtcontact.get(),
        txtaddress.get(1.0, END),
    )
    messagebox.showinfo("Success", "Record Updated")
    clearall()
    displayAll()



def delete_employee():
    db.remove(row[0])
    clearall()
    displayAll()

def clearall():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtaddress.delete(1.0,END)


btn_frame=Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0,columnspan=4, padx=10,pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0,column=0)

btnEdit = Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("calibri", 16, "bold"), fg="white",
                bg="#2980b9", bd=0).grid(row=0,column=1, padx=10)

btnDelete = Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("calibri", 16, "bold"), fg="white",
                bg="#c0392b", bd=0).grid(row=0,column=2, padx=10)

btnClear = Button(btn_frame, command=clearall, text="Clear Details", width=15, font=("calibri", 16, "bold"), fg="white",
                bg="#f39c12", bd=0).grid(row=0,column=3, padx=10)


# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=10, y=480, width=1500, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("calibri", 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("calibri", 18))

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=20)
tv.heading("2", text="NAME")
tv.column("2", width=150)
tv.heading("3", text="AGE")
tv.column("3", width=20)
tv.heading("4", text="D.O.J")
tv.column("4", width=40)
tv.heading("5", text="EMAIL")
tv.column("5", width=200)
tv.heading("6", text="GENDER")
tv.column("6", width=20)
tv.heading("7", text="CONTACT")
tv.column("7", width=50)
tv.heading("8", text="ADDRESS")
tv.column("8", width=300)  # Adjust the width for the ADDRESS column

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getdata)
tv.pack(fill='both', expand=True)


displayAll()
root.mainloop()

