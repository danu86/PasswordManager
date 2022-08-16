from tkinter import *
from tkinter import messagebox

# Create window

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)


# ---------------------------- FUNCTIONS ------------------------------- #


def add_pass():
    with open("passwords.txt", "a") as data:

        # Get the info from entry fields
        website_get = Entry.get(e_website)
        email_username_get = Entry.get(e_website)
        password_get = Entry.get(e_password)

        # Write info into text file
        data.write(f"{website_get}  |  {email_username_get}  |  {password_get} \n")

        # Clear fields after adding them to text file
        e_website.delete(0, END)
        e_emailUsername.delete(0, END)
        e_password.delete(0, END)



# ---------------------------- MAKING THE GUI ------------------------------- #


# Canvas
canvas = Canvas(width=200, height=220, highlightthickness=0)
logo_img = PhotoImage(file="Logo.png")
canvas.create_image(100, 100, image=logo_img)

# Label
website = Label(text="Website:")
emailUsername = Label(text="Email/Username:  ")
password = Label(text="Password")

# Get Users Entries
e_website = Entry(width=51)
e_emailUsername = Entry(width=51)
e_password = Entry(width=33)

# Buttons
genPass = Button(text="Generate Password")
add = Button(text="Add", width=43, command=add_pass)

# ---------------------------- GRID PLACEMENT ------------------------------- #

# Grid Layout
canvas.grid(row=0, column=1)
website.grid(row=1, column=0)
emailUsername.grid(row=2, column=0)
password.grid(row=3, column=0)
e_website.grid(row=1, column=1, columnspan=2)
e_emailUsername.grid(row=2, column=1, columnspan=2)
e_password.grid(row=3, column=1)
genPass.grid(row=3, column=2)
add.grid(row=4, column=1, columnspan=3)

window.mainloop()
