from turtle import Turtle, Screen

def move_forward():
    t.fd(10)


def move_backward():
    t.bk(10)


def turn_left():
    t.lt(10)


def turn_right():
    t.rt(10)

def clear():
    t.clear()
    t.pu()
    t.setpos(0, 0)
    t.pd()


t = Turtle()
screen = Screen()


screen.onkey(key="Up",fun=move_forward)
screen.onkey(key="Down",fun=move_backward)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()