from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.goto(randint(-280, 280), randint(-280, 280))

    def refresh(self):
        self.goto(randint(-280, 280), randint(-280, 280))