from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def counter_clockwise():
    angle = timmy.heading()
    timmy.setheading(angle + 10)


def clockwise():
    angle = timmy.heading()
    timmy.setheading(angle - 10)


def clear():
    timmy.clear()
    timmy.pu()
    timmy.home()
    timmy.pd()


screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
