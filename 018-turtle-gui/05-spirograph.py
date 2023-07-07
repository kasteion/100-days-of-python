import turtle as t
import random as r


def random_color():
    color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
    return color


timmy = t.Turtle()
timmy.speed("fastest")
screen = t.Screen()
t.colormode(255)

for i in range(120):
    timmy.color(random_color())
    timmy.setheading(i*3)
    timmy.circle(100)


timmy.circle(100)

screen.exitonclick()
