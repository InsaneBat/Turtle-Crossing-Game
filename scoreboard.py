from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-270, 270)
        self.level = 1
        self.write(f"Level: {self.level}", True, "left", FONT)

    def refresh(self):
        self.clear()
        self.setposition(-270, 270)
        self.write(f"Level: {self.level}", True, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
