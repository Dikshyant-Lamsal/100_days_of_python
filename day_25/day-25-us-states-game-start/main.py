import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states_temp = data["state"]

states = {"name":[],"coords":{"x":[], "y":[]}}

for state in states_temp:
    states["name"].append(state.lower())
    states["coords"]["x"].append(int(data[data["state"]==state]["x"].iloc[0]))
    states["coords"]["y"].append(int(data[data["state"]==state]["y"].iloc[0]))

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
guessed_states = []
count=0
while True:
    title = f"{count}/50 States Correct"
    prompt = "Guess a State!"
    state = screen.textinput(title=title, prompt=prompt)
    print(state)
    if state == None or count == 50:
        break;
    elif state.lower() == "exit":
        break;
    elif state.lower() not in states["name"]:
        print("Wrong Guess")
    else:
        index = states["name"].index(state.lower())
        writer.goto(states["coords"]["x"][index], states["coords"]["y"][index])
        writer.write(state)
        count+=1
        guessed_states.append(state.lower())

rem_states = [state for state in states["name"] if state not in guessed_states]


states_to_learn = pandas.DataFrame(rem_states)
states_to_learn.to_csv("states_to_learn.csv")


