import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.color("white")
        self.draw_scoreboard()

    def draw_middle(self):
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        for i in range(60):
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(10)

    def draw_score(self):
        self.penup()
        self.goto(0, 230)
        self.write(f"{self.p1_score} \t {self.p2_score}", align="center", font=("Courier", 60, 'normal'))

    def draw_scoreboard(self):
        self.clear()
        self.draw_middle()
        self.draw_score()

    def score_p1(self):
        self.p1_score += 1

    def score_p2(self):
        self.p2_score += 1

