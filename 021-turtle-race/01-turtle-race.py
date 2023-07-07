from turtle import Turtle, Screen
from random import randint


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

s = Screen()
s.setup(width=500, height=400)

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()

for i, color in enumerate(colors):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230, y=i * 30 - 60)
    turtles.append(t)

race_end = False
winner_turtle = ""

while not race_end:
    for turtle in turtles:
        turtle.forward(randint(1, 10))
        if turtle.xcor() >= 230:
            race_end = True
            winner_turtle = turtle.color()[1]

if user_bet == winner_turtle:
    print(f"You've won! The {winner_turtle} is the winner!")
else:
    print(f"You've lost! The {winner_turtle} is the winner!")

s.exitonclick()
