from tkinter import *
import requests


# Functions

def back():
    text.config(bg="white")


def check_right():
    if create() == "True":
        text.config(bg="#95CD41")
    else:
        text.config(bg="#FF5959")
    window.after(1000, back)


def check_left():
    if create() == "False":
        text.config(bg="#95CD41")
    else:
        text.config(bg="#FF5959")
    window.after(1000, back)


def create():

    a = requests.get(url="https://opentdb.com/api.php?amount=2&type=boolean")
    b = a.json()
    c = b["results"][0]["question"]
    answer = b["results"][0]["correct_answer"]
    text.itemconfig(text_new, text=c)

    return answer


# --------------------------------- GUI --------------------------------------------
window = Tk()
window.config(padx=30, pady=50, bg="#062C30")

text = Canvas(bg="#F5F5F5")
text_new = text.create_text(190, 130, fill="#05595B", text="Hi!", width=270, font=("Arial", 20, "normal"), justify="center")
text.grid(column=0, row=0, columnspan=2, pady=40, padx=25)


# Buttons:
# Correct Button
correct_image = PhotoImage(file="true.png")
right = Button(image=correct_image, command=check_right)
right.grid(column=0, row=1, pady=30)

# Wrong Button
wrong_image = PhotoImage(file="false.png")
wrong = Button(image=wrong_image, command=check_left)
wrong.grid(column=1, row=1)


# Start button
start = Button(text="Start", command=create, bg="#A6CF98")
start.grid(columnspan=2, column=0, row=2)


window.mainloop()

