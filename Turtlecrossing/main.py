import time
from turtle import Screen,Turtle
from player import  Player
from carmanager import  Carmanager
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
cars = Carmanager()
score = Scoreboard()

screen.listen()
screen.onkey(player.front,"Up")
screen.onkey(player.back,"Down")

game_is_on = True

while game_is_on:
    time.sleep(0.2)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.cars_list:
        if car.distance(player)<23:
            score.game_over()
            game_is_on = False

    #Detect if player reaches end line
    if player.ycor()>250:
        player.goto(0,-280)
        score.level+=1
        score.update_level()
        cars.level_up()



screen.exitonclick()