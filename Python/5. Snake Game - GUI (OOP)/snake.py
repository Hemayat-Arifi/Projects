from turtle import Turtle
import random


pos_of_x_and_y_food = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180,
                       200, 220, 240, 260, 280, 0, -20, -40, -60, -80,
                       -100, -120, -140, -160, -180,
                       -200, -220, -240, -260, -280]


positions = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake = []
        self.create()
        self.snake[0].xcor()
        self.snake[0].ycor()
        self.a = 0
        self.head = 0
        self.is_on = False
        self.high = 0

    def create(self):
        for square in positions:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(square)
            self.snake.append(new)

        self.snake[0].shape("triangle")
        self.snake[0].color("brown")

    def move(self):
        for _ in range(len(self.snake) - 1, 0, -1):
            x = self.snake[_ - 1].xcor()
            y = self.snake[_ - 1].ycor()
            self.snake[_].goto(x, y)

        self.snake[0].forward(20)
        self.head = self.snake[0]

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(90)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(0)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(270)

    def new(self):
        self.food = Turtle()
        self.food.shape("circle")
        self.food.shapesize(0.9, 0.9)
        self.food.penup()
        self.food.color("green")
        self.food.speed("fastest")
        self.food.goto(random.choice(pos_of_x_and_y_food), random.choice(pos_of_x_and_y_food))

    def clear(self):
        self.food.clear()
        self.food.hideturtle()

    def x_of_snake(self):
        return self.snake[0].xcor()

    def y_of_snake(self):
        return self.snake[0].ycor()

    def x_of_food(self):
        return self.food.xcor()

    def y_of_food(self):
        return self.food.ycor()

    def in_score(self):
        self.a += 1

    def game_over(self):
        self.game = Turtle()
        self.game.color("white")
        self.game.penup()
        self.game.hideturtle()
        self.game.goto(0, 50)
        self.game.write("Game Over !", False, "center", font=("Courier", 35, "bold"))

    def on(self):
        self.is_on = True

    def extend(self):
        new = Turtle("square")
        new.color("white")
        new.penup()
        new.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(new)
