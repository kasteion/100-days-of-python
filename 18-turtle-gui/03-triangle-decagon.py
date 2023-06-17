from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)

for i in range(3, 11):
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
    degrees = 360 / i
    for _ in range(i):
        timmy.forward(100)
        timmy.right(degrees)

screen.exitonclick()
