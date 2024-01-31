import turtle, pandas



data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
img = "blank_states_img.gif"
turtle.addshape(img)

t = turtle.Turtle()
t.shape(img)

w = turtle.Turtle()
w.ht()

score = 0
done = False
all_states = data.state.to_list()
guessed = []
while score < 50 and not done:
    ans = turtle.textinput(title=f"{score}/50 states guessed", prompt="Guess a state!")
    if ans == None:
        done = True
    else:
        ans = ans.title()
        if ans not in guessed and ans in all_states:

            state_data = data[data.state == ans]
            coordinates = (state_data.x.iloc[0], state_data.y.iloc[0])
            w.pu()
            w.goto(coordinates)
            w.pd()
            w.write(ans, align="center")
            w.pu()
            guessed.append(ans)
            score += 1


#states to learn
to_learn = [s for s in all_states if s not in guessed]



outFile = pandas.DataFrame(to_learn)
outFile.to_csv("states_to_learn.csv")

