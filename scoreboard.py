from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, 260)
        self.score_update()
        self.hideturtle()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.score_update()
