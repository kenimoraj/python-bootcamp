import random
import turtle
from turtle import Turtle, Screen

import colorgram


def draw_polygon(turtle,side,n):
    for i in range(n):
        turtle.fd(side)
        turtle.right(360/n)

def dashed_line(turtle):
    for i in range(15):
        turtle.pd()
        turtle.fd(10)
        turtle.pu()
        turtle.fd(10)

def draw_polygon_color(turtle,side,n):
    turtle.pencolor(random_color())
    for i in range(n):
        turtle.fd(side)
        turtle.right(360/n)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)
def random_walk(turtle):
    angles = [0, 90, 180, 270]
    turtle.pensize(15)
    while True:
        turtle.pencolor(random_color())
        angle = random.choice(angles)
        turtle.fd(30)
        turtle.setheading(angle)

def spirograph(turtle, r, n):
    for i in range(n):
        turtle.pensize(5)
        turtle.pencolor(random_color())
        turtle.circle(r)
        turtle.right(360/n)
t = Turtle()
screen = Screen()
screen.colormode(255)
# t.left(90)
t.speed(0)

#Challenge 1

# for i in range(3,11):
#     draw_polygon(t,100,i)

#Challenge 2
# dashed_line(t)

#Challenge 3

# for i in range(3,11):
#     draw_polygon_color(t,100,i)

#Challenge 4 - random  walk
# random_walk(t)

#Challenge 5 - Spirograph
# spirograph(t,200,100)

#Challenge 6 - dots

#Extract colors from hirst.jpg

colors = colorgram.extract("hirst.jpg",30)
color_list = []
for color in colors:
    color_list.append(tuple(color.rgb))
color_list = color_list[2:]
print(color_list)

#drawDots
def dot(t, r, color):
    t.color(color,color)
    t.pu()
    t.rt(90)
    t.fd(r)
    t.lt(90)
    t.pd()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.pu()
    t.lt(90)
    t.fd(r)
    t.rt(90)
    t.pd()
    t.filling()



def drawDots(t):
    t.setheading(90)
    t.pu()
    t.bk(450/2)
    t.right(90)
    t.bk(450/2)
    t.pd()
    for i in range(10):
        for j in range(10):
            color = random.choice(color_list)
            dot(t,10,color)
            t.pu()
            t.fd(50)
            t.pd()
        t.pu()
        t.lt(90)
        t.fd(50)
        t.rt(90)
        t.bk(500)

t.ht()
drawDots(t)
screen.exitonclick()

