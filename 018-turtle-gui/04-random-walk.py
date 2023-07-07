from turtle import Turtle, Screen
import random

angles = [0, 90, 180, 270]

timmy = Turtle()
screen = Screen()
screen.colormode(255)


def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return color


timmy.width(10)
timmy.speed('fastest')
for _ in range(500):
    timmy.setheading(random.choice(angles))
    timmy.color(random_color())
    timmy.forward(15)


screen.exitonclick()
