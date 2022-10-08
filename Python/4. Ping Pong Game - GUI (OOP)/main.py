from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scores import Score


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("white")
screen.title(' ' * 90 + "--- Hemo Gak Ping Pong Game ---")
screen.tracer(1)


paddle_1 = Paddle(350, 0)
score_1 = Score(-100, 210)

paddle_2 = Paddle(-350, 0)
score_2 = Score(50, 210)

time.sleep(0.5)

ball = Ball()

time.sleep(0.5)


screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")
screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")


is_on = True
while is_on:
    screen.update()

    ball.move()

    # TODO: COLLISION WITH WALLS DETECTED & SOLVED
    if ball.ball.ycor() > 280 or ball.ball.ycor() < -280:
        ball.bounce_y()

    # TODO: COLLISION WITH PADDLES_1 DETECTED & SOLVED
    if ball.ball.distance(paddle_1.hemo) < 50 and ball.ball.xcor() > 320:
        ball.bounce_x()

    # TODO: COLLISION WITH PADDLES_2 DETECTED & SOLVED
    if ball.ball.distance(paddle_2.hemo) < 70 and ball.ball.xcor() > -340:
        ball.bounce_x()

    # TODO: BALL OUT OF BOND DETECTION & SOLUTION --> Right Paddle
    if ball.ball.xcor() >= 380:
        score_1.scoring()
        time.sleep(0.5)
        ball.clear()

    # TODO: BALL OUT OF BOND DETECTION & SOLUTION --> Left Paddle
    if ball.ball.xcor() <= -380:
        score_2.scoring()
        time.sleep(0.5)
        ball.clear()

    if score_1.scored == 2:
        ball.ball.speed("normal")
    elif score_1.scored == 3:
        ball.ball.speed("fast")
    elif score_1.scored == 4:
        ball.ball.speed("fastest")





screen.exitonclick()
