from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_score()
        self.color("white")
        self.penup()
        self.goto((0, 260))
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Comic Sans', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        with open("data.txt") as file:
            temp = file.read()
            self.high_score = int(temp)

    def write_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")


    # def game_over(self):
    #     self.goto((0, 0))
    #     self.write("Game Over", align="center", font=('Comic Sans', 24, 'normal'))
