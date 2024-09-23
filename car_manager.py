from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        random_y = random.randint(-250, 250)
        self.speed("fastest")
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.setposition(300, random_y)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)

    def move(self, level):
        increment = level - 1
        increment = MOVE_INCREMENT * increment
        self.forward(STARTING_MOVE_DISTANCE + increment)
