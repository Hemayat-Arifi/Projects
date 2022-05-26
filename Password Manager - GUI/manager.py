from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ------------------------------- Password Generator ----------------------------------


def gen():
    a = random_pass()
    password_entry.delete(0, END)
    password_entry.insert(0, a)
    pyperclip.copy(a)


def random_pass():

    import random
    alphabets = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                 "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                 "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["!", "$", "#", "%", "@", "&", "*"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    password = []

    for al in range(1, random.randint(3, 7) + 1):
        password += random.choice(alphabets)
    for no in range(1, random.randint(2, 4) + 1):
        password += random.choice(numbers)
    for sy in range(1, random.randint(2, 4) + 1):
        password += random.choice(symbols)

    random.shuffle(password)

    new = ""
    for i in password:
        random.choice(password)
        new += i

    return new


# ------------------------------- Search in Data --------------------------------------

def search():
    web = web_entry.get()
    try:
        with open("password.json", "r") as file:
            searched_file = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File Data not found")
    else:
        if web in searched_file:
            messagebox.showinfo(title=f"Your info for {web} ", message=f"your email {searched_file[web]['email']}\n"
                                                                       f"your password {searched_file[web]['password']}")
        elif web not in searched_file:
            messagebox.showinfo(title="Hmmm?", message="not matched")


# ------------------------------- Save Password ---------------------------------------


def append(event):

    web = web_entry.get()
    e_mail = email_entry.get()
    pass_word = password_entry.get()

    password_dic = {
        web: {
            "email": e_mail,
            "password": pass_word,
        },
    }

    if len(email_entry.get()) < 5 or len(password_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showerror(message="Too short or empty!")

    else:

        try:

            with open("password.json", mode="r") as file:
                data = json.load(file)
                data.update(password_dic)
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

                with open("password.json", mode="w") as file:
                    json.dump(data, file, indent=4)

        except FileNotFoundError:

            with open("password.json", mode="a") as file:
                json.dump(password_dic, file, indent=4)
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

# ------------------------------- G - U - I -------------------------------------------------


window = Tk()
window.config(padx=25, pady=0, bg="#112031")
window.minsize(width=400, height=380)
window.maxsize(width=500, height=500)
window.title("                                                    Hemo Password Manager")


canvas = Canvas(width=475, height=200, bg="#112031", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(220, 100, image=logo)
canvas.grid(column=0, row=0, pady=30, columnspan=3)


# Web Label
website = Label(text="Web Site", bg="#112031", fg="#D4ECDD", font=("Arial", 13, "bold"))
website.grid(column=0, row=1)


# Website Entry
web_entry = Entry(width=24)
web_entry.grid(column=1, row=1, pady=10)
web_entry.focus()


# Search Button
search_button = Button(text="Search", padx=40, font=("Arial", 9, "normal"), command=search, bg="#112031", fg="#D4ECDD")
search_button.grid(column=2, row=1)


# Email Label
email = Label(text="Email Add", bg="#112031", fg="#D4ECDD", font=("Arial", 13, "bold"))
email.grid(column=0, row=2, padx=10)


# Email Entry
email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2, pady=10)


# Password Label
password_label = Label(text="Password", bg="#112031", fg="#D4ECDD", font=("Arial", 13, "bold"))
password_label.grid(column=0, row=3)


# Password Entry
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)


# Generate Password Button
Generate = Button(text="Generate Password", pady=3, font=("Arial", 9, "normal"), command=gen, bg="#112031", fg="#D4ECDD")
Generate.grid(column=2, row=3, pady=10)


# Submit Button
submit = Button(text="Add", width=42, command=append, bg="#345B63", fg="#D4ECDD", font=("Arial", 9, "bold"))
submit.grid(column=1, row=4, columnspan=2, pady=25)
submit.bind("<Return>", append)


window.mainloop()

