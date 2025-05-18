from turtle import Turtle
import random

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.color('deep pink')
        self.hideturtle()
        self.increse_point()


    def increse_point(self):
        self.clear()
        style = ('Courier', 15, 'italic')
        self.write(f'Score:{self.score}', font=style, align='center')

    def game_over(self):
        self.goto(0,0 )
        style = ('Courier', 15, 'italic')
        self.write("Game Over", font=style, align='center')
