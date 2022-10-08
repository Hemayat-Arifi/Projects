from turtle import Turtle


class Ball:

    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.shapesize(1, 1)
        self.ball.penup()
        self.ball.color("brown")
        self.ball.speed("slowest")
        self.ball_x = 10
        self.ball_y = 10

    def move(self):
        self.new_x = self.ball.xcor() + self.ball_x
        self.new_y = self.ball.ycor() + self.ball_y
        self.ball.goto(self.new_x, self.new_y)

    def bounce_y(self):
        self.ball_y *= -1

    def bounce_x(self):
        self.ball_x *= -1

    def clear(self):
        self.ball.hideturtle()
        self.ball.home()
        self.ball.showturtle()
