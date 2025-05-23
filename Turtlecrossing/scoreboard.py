from  turtle import  Turtle

FONT = ("Courier",24,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.goto(0,260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=("Courier", 24, "bold"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 30, "bold"))
