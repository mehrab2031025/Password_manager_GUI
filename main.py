import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,"end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for j in range(randint(2, 4))]
    password_list += [choice(numbers) for k in range(randint(2, 4))]

    shuffle(password_list)
    string = "".join(password_list)
    password_entry.insert(0,string)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or website == "" or password == "":
        messagebox.showinfo(title="Blank ERROR", message="Please provide necessary data")

    else:
        ok = messagebox.askyesno(title="Confirmation", message=f"Do you like to save\n"f"email: "
                                                               f"{email}\npassword: {password}\nfor\nwebsite: "
                                                               f"{website}")
        if ok:
            with open("file.txt", 'a') as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
img = tk.PhotoImage(file="logo1.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website: ")
website_label.grid(column=0, row=1)

website_entry = tk.Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = tk.Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_entry = tk.Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password_label = tk.Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = tk.Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=43, command=add_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
