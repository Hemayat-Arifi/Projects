import tkinter as tk
from time import perf_counter


class App:
    def __init__(self):
        self.root = tk.Tk()

        self.text = tk.Text(self.root)
        self.text.pack()
        self.text.bind("<Key>", self.text_entered)

        self.text.after(100, self.check_clear_text)
        self.time_last_written = perf_counter()

        self.root.mainloop()

    def text_entered(self, event):
        self.time_last_written = perf_counter()

    def clear_text(self):
        print("Le text vient d'etre détruit")
        # Delete all of the text
        self.text.delete("0.0", "end")

    def check_clear_text(self):
        time_diff = perf_counter() - self.time_last_written
        print(f"Last key pressed: {time_diff} sec ago.")
        if time_diff > 5: # The 5 is in seconds
            self.clear_text()
        self.text.after(100, self.check_clear_text)


app = App()

















































# from tkinter import *
#
#
# # __________________ The User Interface
# win = Tk()
# win.config(pady=50, padx=50)
#
#
# # __________________ Entry Field
# notes = Text(width=50, height=15, font=("Arial", 20, "bold"), bg="silver", fg="black")
# notes.grid(column=0, row=0)
#
#
# def yes():
#     notes.delete("1.0", "end-1c")
#
#
# def clear():
#     print(notes.get("1.0", "end-1c"))
#     win.after(5000, yes)
#     print(notes.get("1.0", "end-1c"))
#     clear()
#
#
# clear()
#
#
# win.mainloop()



