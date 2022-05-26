from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("brown")
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(-220, 250)
        self.write(f" Level = {self.score}", False, "center", font=("Courier", 20, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f" Level = {self.score}", False, "center", font=("Courier", 20, "bold"))