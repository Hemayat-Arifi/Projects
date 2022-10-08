from turtle import Screen, Turtle
import time
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)


hemo = Snake()

hemo.new()

score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 270)
score.write(f"Score = {hemo.a}", False, "center", font=('Arial', 15, 'normal'))


screen.listen()
screen.onkey(hemo.up, "Up")
screen.onkey(hemo.left, "Left")
screen.onkey(hemo.down, "Down")
screen.onkey(hemo.right, "Right")
screen.onkey(hemo.right, "Right")


hemo.on()


while hemo.is_on:
    screen.update()
    time.sleep(0.1)

    hemo.move()

    # TODO: Collision with tail detected
    for s in hemo.snake[1:]:
        if hemo.head.distance(s) < 10:
            hemo.is_on = False
            hemo.game_over()

    # TODO: Collision with wall detected
    if hemo.head.xcor() >= 300 or hemo.head.xcor() <= -300:
        is_on = False
        hemo.game_over()
        screen.update()
        break
    elif hemo.head.ycor() >= 300 or hemo.head.ycor() <= -300:
        is_on = False
        hemo.game_over()
        screen.update()
        break

    # TODO: Collision with food detected
    if hemo.x_of_snake() <= hemo.x_of_food() + 3:
        if hemo.y_of_snake() <= hemo.y_of_food() + 3:
            if hemo.x_of_snake() >= hemo.x_of_food() - 3:
                if hemo.y_of_snake() >= hemo.y_of_food() - 3:
                    score.clear()
                    hemo.extend()
                    hemo.clear()
                    hemo.new()
                    hemo.in_score()
                    score.write(f"Score = {hemo.a}", False, "center", font=('Arial', 15, 'normal'))


screen.exitonclick()
