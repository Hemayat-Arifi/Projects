from turtle import Turtle


class Score(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.scored = 0
        self.hideturtle()
        self.color("darkred")
        self.penup()
        self.goto(x, y)
        self.score_board()

    def score_board(self):
        self.write(f"{self.scored}", False, font=("Arial", 50, "normal"))

    def scoring(self):
        self.clear()
        self.scored += 1
        self.write(f"{self.scored}", False, font=("Arial", 60, "normal"))
