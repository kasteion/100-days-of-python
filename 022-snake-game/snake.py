from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(0, 3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            if i > 0:
                t.setx(self.body[i - 1].xcor() - 20)
            self.body.append(t)

    def move_forward(self):
        prev_pos = [0, 0]
        for i, chunk in enumerate(self.body):
            curr_pos = [chunk.xcor(), chunk.ycor()]
            if i == 0:
                chunk.forward(MOVE_DISTANCE)
            else:
                chunk.goto(prev_pos[0], prev_pos[1])
            prev_pos = curr_pos

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        last_chunk = self.body[-1]
        t.goto(last_chunk.pos())
        self.body.append(t)

    def reset(self):
        for chunk in self.body:
            chunk.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
