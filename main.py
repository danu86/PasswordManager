from tkinter import *
from tkinter import messagebox

# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=100)


# ---------------------------- FUNCTIONS ------------------------------- #

def pass_generator():
    import string
    import random

    # Make empty variable to store password
    gen_pass = ""

    # Make a for loop that creates 20 random characters and adds them to gen_pass variable
    for _ in range(20):
        char = random.choice(string.ascii_letters + string.punctuation + string.digits)
        gen_pass += char

    # Empty password entry field and insert generated password
    e_password.delete(0, END)
    e_password.insert(0, gen_pass)

    # Copy the password to clipboard
    window.clipboard_clear()
    window.clipboard_append(gen_pass)


def save_data():
    # Make a text file and open it (as append)
    with open("passwords.txt", "a") as data:

        # Get the info from entry fields
        website_get = Entry.get(e_website)
        email_username_get = Entry.get(e_website)
        password_get = Entry.get(e_password)

        # Ask user to confirm data
        confirmation = messagebox.askokcancel(title=website_get, message=f"Email/Username: {email_username_get} \n"
                                                                         f"Password: {password_get} \n"
                                                                         f"Is this ok?")

        # If confirmed, write info into text file
        if confirmation:
            data.write(f"{website_get}  |  {email_username_get}  |  {password_get} \n")

            # Clear fields after adding them to text file
            e_website.delete(0, END)
            e_emailUsername.delete(0, END)
            e_password.delete(0, END)

        # If not confirmed, pass
        else:
            pass


# ---------------------------- MAKING THE GUI ------------------------------- #


# Canvas
canvas = Canvas(width=200, height=230, highlightthickness=0)
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
genPass = Button(text="Generate Password", command=pass_generator)
add = Button(text="Add", width=43, command=save_data)

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
