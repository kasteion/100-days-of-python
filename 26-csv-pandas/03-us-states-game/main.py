import turtle
import pandas

s = turtle.Screen()
s.title("U.S. States Game")
image = "blank_states_img.gif"
s.addshape(image)

t = turtle.Turtle()
t.shape(image)

df = pandas.read_csv("50_states.csv")

text_t = turtle.Turtle()
text_t.penup()
text_t.hideturtle()


correct_states = []

while len(correct_states) < 50:
    user_input = s.textinput(title=f"{len(correct_states)}/50 states correct", prompt="What's another state name?")
    if user_input is None:
        break
    else:
        user_input = user_input.title()
    state = df[df.state == user_input]
    if len(state) > 0:
        # text_t.goto(state.iloc[0].x, state.iloc[0].y)
        text_t.goto(state.x.item(), state.y.item())
        text_t.write(state.state.item())
        if user_input not in correct_states:
            correct_states.append(user_input)

states_to_learn = df[~df.state.isin(correct_states)].filter(items=["state"])
states_to_learn.to_csv("states_to_learn.csv")

# turtle.mainloop()
