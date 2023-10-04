import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
cars = []

score_board = Scoreboard()
p1 = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(p1.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()

    car_manager.move_left()

    for car in car_manager.cars:
        if car.distance(p1) < 25:
            game_is_on = False
            score_board.game_over()

    if p1.ycor() > 290:
        p1.reset_position()
        score_board.increase_level()
        car_manager.level += 1

screen.exitonclick()
