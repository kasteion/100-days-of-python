import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()

screen.onkey(key="Up", fun=player.move_forward)

tick = 0
game_is_on = True
sleep = 0.1

while game_is_on:
    time.sleep(sleep)
    screen.update()

    tick += 1
    if tick % 5 == 0:
        tick = 0
        cars.create_car()

    cars.move_forward()

    for car in cars.cars:
        if player.distance(car) < 20 and abs(car.ycor() - player.ycor()) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() >= FINISH_LINE:
        score.next_level()
        # cars.next_level()
        sleep *= 0.5
        player.reset_position()

screen.exitonclick()
