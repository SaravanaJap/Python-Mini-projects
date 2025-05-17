import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Turtle race",prompt="Which turtle will win the game?Pick a color from rainbow:")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
race_on = False
x = -230
y = -160
turtles = []
for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.goto(x,y)
    y+=50

if user_bet:
    race_on = True

while race_on:

    for i in turtles:
        if i.xcor()>230:
            race_on = False
            winner = i.pencolor()
            if winner == user_bet.lower():
                print("You won")
            else:
                print(f"You lost winner is {winner}")
            break
        distance = random.randint(0, 20)
        i.forward(distance)


screen.exitonclick()