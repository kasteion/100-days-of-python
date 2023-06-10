from turtle import Turtle, Screen
import random as r
import colorgram


def extract_colors():
    colors = colorgram.extract('image.jpeg', 20)
    color_l = []
    for color in colors:
        color_t = (color.rgb[0], color.rgb[1], color.rgb[2])
        color_l.append(color_t)
    return color_l


colors = extract_colors()

timmy = Turtle()
screen = Screen()

screen.colormode(255)

timmy.speed("fastest")
timmy.hideturtle()
timmy.pu()
timmy.goto(-220, -220)

for _ in range(10):
    for _ in range(10):
        timmy.dot(20, r.choice(colors))
        timmy.goto(timmy.xcor() + 50, timmy.ycor())
    timmy.goto(timmy.xcor() - 500, timmy.ycor() + 50)

screen.exitonclick()
