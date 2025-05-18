from turtle import Screen
from  paddle import  Paddle
from  ball import Ball
import time
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

#Creating paddles
left_paddle = Paddle((-380,0))
left_paddle.speed('fastest')
right_paddle = Paddle((380,0))
right_paddle.speed('fastest')

#Creating ball
ball = Ball()


scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up,"W")
screen.onkey(left_paddle.down,"S")
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280  :
        ball.bounce_y()

    #Detect collision with right_paddle

    if ball.distance(right_paddle)<40 and ball.xcor()>340 or ball.distance(left_paddle)<40 and ball.xcor()<-340:
        ball.ball_speed *= 0.9
        ball.bounce_x()

    #Detect if right paddle misses

    if ball.xcor()>400:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.left_score >= 2:
            scoreboard.game_over("Left")
            game_is_on = False

    # Detect if left paddle misses
    if ball.xcor()< -400:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.right_score >= 2:
            scoreboard.game_over("Right")
            game_is_on = False



screen.exitonclick()