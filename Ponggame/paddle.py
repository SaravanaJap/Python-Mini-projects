from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,coordinate):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=4,stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(coordinate)

    def up(self):
        self.sety(self.ycor() + 10)
    def down(self):
        self.sety(self.ycor() - 10)

