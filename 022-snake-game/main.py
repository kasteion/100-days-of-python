import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
s.listen()

snake = Snake()
s.update()

s.onkey(key='Up', fun=snake.up)
s.onkey(key='Down', fun=snake.down)
s.onkey(key='Left', fun=snake.left)
s.onkey(key='Right', fun=snake.right)

food = Food()
score = ScoreBoard()

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move_forward()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.eat()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_scoreboard()
        snake.reset()

    for chunk in snake.body[1:]:
        if snake.head.distance(chunk) < 10:
            score.reset_scoreboard()
            snake.reset()
            # score.game_over()
            # is_game_on = False

s.exitonclick()
