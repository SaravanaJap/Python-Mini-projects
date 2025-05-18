import turtle
import colorgram
from snake import  Snake
import time
from turtle import  Turtle,Screen
from food import Food
from scoreboard import Scoreboard

turtle.colormode(255)
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor(128,255,128)
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        snake.extend()
        scoreboard.score+=1
        scoreboard.increse_point()
        food.refresh()
        print(scoreboard.score)
    #Detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()< -285 or snake.head.ycor()>285 or snake.head.ycor()< -285:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False









screen.exitonclick()