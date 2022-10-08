from turtle import Turtle


class Paddle:

    def __init__(self, a, b):
        self.hemo = Turtle()
        self.hemo.shape("square")
        self.hemo.shapesize(1, 5)
        self.hemo.penup()
        self.hemo.color("teal")
        self.hemo.setheading(90)
        self.hemo.goto(a, b)
        self.hemo.speed("fastest")

    def move_up(self):
        self.hemo.forward(50)

    def move_down(self):
        self.hemo.back(50)
