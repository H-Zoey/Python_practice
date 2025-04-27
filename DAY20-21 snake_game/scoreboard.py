from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 17, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        #self.hideturtle()

    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
