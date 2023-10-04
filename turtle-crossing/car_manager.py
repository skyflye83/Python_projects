import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        #super().__init__()
        self.cars = []
        self.level = 0

    def add_car(self):
        random_choice = random.randint(1, 5)
        if random_choice == 5:
            y_axis = range(-250, 250, 40)
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(COLORS[random.randint(0, 5)])
            car.setheading(180)
            car.goto(300, random.choice(y_axis))
            car.shapesize(1, 2)
            self.cars.append(car)

    def move_left(self):
        for car in self.cars:
            step = (MOVE_INCREMENT * self.level) + STARTING_MOVE_DISTANCE
            car.forward(step)


