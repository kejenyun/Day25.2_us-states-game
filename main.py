import turtle
import pandas

screen = turtle.Screen()
screen.title("US. State Game")
image = "blank_states_img.gif"
screen.addshape(image) # add graphic as one of turtle type to show the graphic on the screen
turtle.shape(image)


data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list() # convert series to list so we can work with
guessed_states =[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # state-to_learn.csv
        state_to_learn = [ state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states: # find the item that's not in the list
        #         state_to_learn.append(state)
        new_data = pandas.DataFrame(state_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:  #create a turtle from a Turtle class
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #pull out the row that the answer state exist,
        # then you can pull out the X, and y
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)







