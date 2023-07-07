from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(37)

    def move_forward(self):
        self.forward(20)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce()
        self.move_speed = 0.1

    def bounce(self):
        self.move_speed *= 0.9
        if 0 <= self.heading() < 90:
            if self.ycor() < 280:
                self.setheading(randint(120, 180))
            else:
                self.setheading(randint(300, 330))
        elif 90 <= self.heading() < 180:
            if self.ycor() < 280:
                self.setheading(randint(0, 60))
            else:
                self.setheading(randint(210, 240))
        elif 180 <= self.heading() < 270:
            if self.ycor() > -280:
                self.setheading(randint(300, 360))
            else:
                self.setheading(randint(120, 150))
        elif 270 <= self.heading() < 360:
            if self.ycor() > -280:
                self.setheading(randint(180, 240))
            else:
                self.setheading(randint(30, 60))
