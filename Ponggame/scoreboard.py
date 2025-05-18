from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()
        self.show_title()

    def show_title(self):
        self.goto(0, 260)
        self.write("PONG", align="center", font=("Courier", 24, "bold"))


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 70, "normal"))

    def l_point(self):
        self.left_score+=1
        self.update_scoreboard()
    def r_point(self):
        self.right_score+=1
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"Game Over! {winner} Wins!", align="center", font=("Courier", 30, "bold"))


