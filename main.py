import turtle
import pandas

#screen setup
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#state guessed list
states_guessed  = []
#count number of states guessed
states_count = 0
#read csv data
data = pandas.read_csv("50_states.csv")
#Converting CSV data to list
state = data.state.to_list()
while states_count < 50:
    answer = screen.textinput(title=f"{states_count}/50 states", prompt="What is the another States Name??").title()
    #giving exit feature to user
    if answer == "Exit":
        for states in states_guessed:
            state.remove(states)
        df = pandas.DataFrame(state)
        df.to_csv("States to learn.csv")
        break
     #answer checking
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
