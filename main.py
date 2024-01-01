import turtle
import pandas

screen = turtle.Screen()
screen.title("US state Game")
image = "blank_states_img.gif"
screen.addshape(image)
data = pandas.read_csv("50_states.csv")
turtle.shape(image)

score = 0
guessed_states = []
while score < 50:
    state_name = turtle.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")
    if state_name.lower() == "exit":
        all_states = data.state.to_list()
        states_to_learn = []
        for city in all_states:
            if city not in guessed_states:
                states_to_learn.append(city)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    selected_state_series = data[data.state == state_name.title()]
    if selected_state_series.size > 0 and (state_name.title() not in guessed_states):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        score += 1
        guessed_states.append(state_name.title())
        x = selected_state_series.x
        y = selected_state_series.y
        t.goto(int(x), int(y))
        t.write(state_name)
