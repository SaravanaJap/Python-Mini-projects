from turtle import  Turtle
MOVE_DISTANCE = 20
COORDINATES = [0,-20,-40]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            snake = Turtle(shape='square')
            snake.penup()
            snake.goto(COORDINATES[i], 0)
            self.segments.append(snake)

    def add_segment(self,position):
        snake = Turtle(shape='square')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)