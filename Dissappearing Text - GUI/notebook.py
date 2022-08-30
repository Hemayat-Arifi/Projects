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
        print("Some random text for test")
        # Delete all of the text
        self.text.delete("0.0", "end")

    def check_clear_text(self):
        time_diff = perf_counter() - self.time_last_written
        print(f"Last key pressed: {time_diff} sec ago.")
        if time_diff > 5: # The 5 is in seconds
            self.clear_text()
        self.text.after(100, self.check_clear_text)


app = App()

