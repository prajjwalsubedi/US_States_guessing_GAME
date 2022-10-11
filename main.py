import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_guessed  = []
states_count = 0
data = pandas.read_csv("50_states.csv")
state = data.state.to_list()
while states_count < 50:
    answer = screen.textinput(title=f"{states_count}/50 states", prompt="What is the another States Name??").title()
    if answer == "Exit":
        for states in states_guessed:
            state.remove(states)
        df = pandas.DataFrame(state)
        df.to_csv("States to learn.csv")
        break
    if answer in state:
        answer_row = data[data.state == answer]
        tim = turtle.Turtle()
        tim.pu()
        tim.hideturtle()
        tim.goto(int(answer_row.x), int(answer_row.y))
        tim.write(f"{answer}", font=('Arial', 8, 'normal'))
        states_count += 1
        states_guessed.append(answer)

screen.exitonclick()
