import colorgram
import turtle as turt
import random
from turtle import Screen
turt.colormode(255)

colors = colorgram.extract('Hirst_dot_paint.jpg',30)
colors_list = []
for color in colors:
    new_color = (color.rgb.r,color.rgb.g,color.rgb.b)
    colors_list.append(new_color)

turtle1 = turt.Turtle()
turtle1.speed('fastest')
turtle1.hideturtle()

turtle1.penup()
x=-200
y=-200

while y!=300:
    turtle1.goto(x,y)

    for i in range(10):
        turtle1.dot(20, random.choice(colors_list))
        turtle1.forward(40)
    y+=50







screen = Screen()
screen.exitonclick()


