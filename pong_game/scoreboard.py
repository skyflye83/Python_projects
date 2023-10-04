from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=("Courier", 20, "normal"))

    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=("Courier", 20, "normal"))

    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score}     {self.r_score}", align="center", font=("Courier", 20, "normal"))
