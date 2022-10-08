import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


hemo = Player()

score = Scoreboard()
screen.update()

car = CarManager()
car.hideturtle()


screen.listen()
screen.onkey(hemo.move, "Up")

screen.onkey(hemo.moved, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if hemo.ycor() >= 280:
        hemo.restart()
        score.update_score()
        time.sleep(0.5)

    for i in car.cars:
        if hemo.distance(i) < 30:
            if i.ycor() - 5 >= hemo.ycor() or i.ycor() + 5 <= hemo.ycor():
                print(i.ycor())
                game_is_on = False

    car.create()
    car.move()


screen.exitonclick()