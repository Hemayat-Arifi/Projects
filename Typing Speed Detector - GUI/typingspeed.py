from tkinter import *
import time
import random


# ______________ Functions
first = 0
final = 0
result = 0

text_list = ["This project is open source\nyou can check your typing speed very easy", "Some random sentences\nin order to perform multiple tests on user experiences."]



def start_btn():
    global first
    a = time.time()
    first = a


def end_btn():
    global final
    b = time.time()
    final = b


def check_btn():
    global result
    user_typed_string = user.get("1.0", 'end-1c')
    user_typed_characters = len([n for n in user_typed_string if n != " "])
    problem = final - first
    result = round(problem, 2)
    text.config(text=random.choice(text_list))


    # Formula
    seconds_2_minute = result / 60
    a = round((user_typed_characters / 5) / seconds_2_minute, 2)
    print(a)

    dashboard = Label(text=f"Your typing speed is {a} WPM.", font=("Arial", 15, "bold"), fg="teal")
    dashboard.grid(column=0, columnspan=2, row=4)


# ______________ The GUI
win = Tk()
win.config(pady=50, padx=50)

# ______________ The Text to be typed
text = Label(text="Hello World!\n this program is written in python programming language", font=("Arial", 20, "bold"), fg="gold", bg="gray", width=50)
text.grid(column=0, row=0, columnspan=2)


# ______________ Input Entry where user type
user = Text(width=50, height=5, font=("Arial", 15, "bold"), bg="silver")
user.grid(column=0, row=1, pady=50, columnspan=2)
user.focus()


# ______________ Start & End Buttons
start = Button(text="Start", command=start_btn, bg="green", font=("arial", 10, "bold"), width=20)
start.grid(column=0, row=2)

end = Button(text="End", command=end_btn, font=("arial", 10, "bold"), width=20, bg="darkred")
end.grid(column=1, row=2)

check = Button(text="Check Score", command=check_btn, font=("arial", 10, "bold"), width=20, bg="teal")
check.grid(column=0, row=3, columnspan=2, pady=25)


win.mainloop()
