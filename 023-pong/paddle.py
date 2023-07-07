from turtle import Turtle

PADDLE_SIZE = 6


class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.create_body(initial_position)

    def create_body(self, initial_position):
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        print(self.get_shapepoly())
        self.penup()
        self.goto(initial_position)

    def move_up(self):
        if self.ycor() < 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
