from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game - By Axel Alvarado")
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
screen.onkey(player.move, "w")

cars = []
loops = 0
game_is_on = True
while game_is_on:
    random_chance = random.randint(1, 6)
    time.sleep(.1)
    if random_chance == 1:
        cars.append(CarManager())
    screen.update()
    for car in cars:
        car.move(scoreboard.level)
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 285:
        player.refresh()
        scoreboard.level += 1
        scoreboard.refresh()

    loops += 1

screen.exitonclick()