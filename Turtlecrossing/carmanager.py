from turtle import Turtle
import random
COLORS = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Carmanager():

    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            x=300
            y = random.randint(-250,250)
            new_car.goto(x,y)
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT




