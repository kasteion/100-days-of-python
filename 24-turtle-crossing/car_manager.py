from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(300, randint(-250, 280))
        car.color(choice(COLORS))
        self.cars.append(car)

    def move_forward(self):
        for i, car in enumerate(self.cars):
            car.clear()
            car.forward(self.move_distance)
            if car.xcor() < -320:
                self.cars.pop(i)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT
