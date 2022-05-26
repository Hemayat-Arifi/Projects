from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(725, 491)

screen.bgpic("blank_states_img.gif")

text = Turtle()
text.hideturtle()
text.penup()

score = 0

text_score = Turtle()
text_score.hideturtle()
text_score.penup()
text_score.goto(-150, 210)
text_score.write(f"Score = {score}/50", False, "center", font=("Arial", 18, "bold"))

state_data = pandas.read_csv("50_states.csv")
state_name = state_data["state"].tolist()

guessed_right = []

game = True

while game:
    player_guess = screen.textinput(title="Guess the State", prompt="Write the name?").title()

    if player_guess in state_name:
        s = state_data[state_data.state == player_guess]
        text.goto(int(s["x"]), int(s["y"]))
        text.write(player_guess, False, "center", font=("Arial", 10, "bold"))
        score += 1
        text_score.clear()
        text_score.write(f"Score = {score}/50", False, "center", font=("Arial", 18, "bold"))
        guessed_right.append(player_guess)

    if score == 50:
        game = False
        break

    if player_guess == "Exit":
        game = False
        for i in state_name:
            if i not in guessed_right:
                with open("remained_states.csv", "a") as file:
                    file.write(f"{i}\n")
        break


screen.exitonclick()
