from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

P1_INITIAL_POSITION = (-360, 0)
P2_INITIAL_POSITION = (350, 0)

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)
s.listen()

p1 = Paddle(P1_INITIAL_POSITION)
p2 = Paddle(P2_INITIAL_POSITION)
ball = Ball()
score = Scoreboard()

s.onkey(key='w', fun=p1.move_up)
s.onkey(key='s', fun=p1.move_down)
s.onkey(key='Up', fun=p2.move_up)
s.onkey(key='Down', fun=p2.move_down)

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    s.update()

    if ball.distance(p1) < 50 and ball.xcor() < -330 or ball.distance(p2) < 50 and ball.xcor() > 320:
        ball.bounce()

    if ball.ycor() > 280 or ball.ycor() <= -280:
        ball.bounce()

    if ball.xcor() > 400:
        score.score_p1()
        ball.reset_position()

    if ball.xcor() < -400:
        score.score_p2()
        ball.reset_position()

    ball.move_forward()
    score.draw_scoreboard()

s.exitonclick()
