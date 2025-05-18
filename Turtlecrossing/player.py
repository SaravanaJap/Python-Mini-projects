from turtle import  Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 200



class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def front(self):
        self.forward(MOVE_DISTANCE)

    def back(self):
        self.backward(MOVE_DISTANCE)