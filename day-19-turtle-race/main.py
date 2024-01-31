from turtle import Turtle, Screen
import random
#setup
screen = Screen()
screen.setup(500,400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]

turtles = []
for i in range(len(colors)):
    turtle = Turtle()
    turtle.shape("circle")
    turtle.color(colors[i])
    turtle.pu()
    turtle.setpos(-230,-140 + 50*i)
    turtles.append(turtle)

bet = screen.textinput("Place your bet", "Which turtle is going to win?")
print(f"You bet \'{bet}\'")

#race
done = False
while not done:
    for i in range(len(turtles)):
        t = turtles[i]
        t.fd(random.randint(0, 1)*10)
        if t.xcor() > 220:
            done = True
            break
print(f"{colors[i].title()} turtle won.")
#results

#end
screen.exitonclick()