import turtle
import pandas

# Make the screen and place an image on it for the quiz.
screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

# Read the csv file and place it in a variable.
data = pandas.read_csv("50_states.csv")
correct_guesses = []
state_list = data.state.to_list()

game_on = True
while game_on:
    # Get a prompt box that gets input from the user.
    state_answer = screen.textinput(f"{len(correct_guesses)} out of 50 States Correct", "What's another state's name:  ").title()
    # Check if the guess is among the state data
    if state_answer in state_list:
        state_data = data[data.state == state_answer]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x_cor, y_cor)
        new_turtle.write(state_answer)
        if state_answer not in correct_guesses:
            correct_guesses.append(state_answer)
    elif state_answer == "Exit":
        game_on = False
        states_not_known = ["States"]
        for state in state_list:
            if state not in correct_guesses:
                states_not_known.append(state)
        df = pandas.DataFrame(states_not_known)
        df.to_csv("states_to_learn.csv")


