import turtle
from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self, length, segment_size, color):
        self.head = Turtle()
        self.color = color
        self.segment_size = segment_size
        self.dead = False
        self.interrupted = False
        self.turns = []
        ss = self.segment_size/2
        ratio = 1/3
        turtle.addshape("head", (
            (-ss, -ss), (-ss, ss), (-ss * 2*ratio, ss), (-ss * 2*ratio, ss * 2*ratio), (-ss * ratio, ss * 2*ratio),
            (-ss * ratio, ss), (ss*ratio, ss), (ss*ratio, ss*2*ratio), (ss*2*ratio, ss*2*ratio), (ss*2*ratio, ss), (ss, ss), (ss, -ss)))
        self.head.shape("head")
        self.head.color(self.color)
        self.head.pu()
        self.tail = []
        for _ in range(length-1):
            self.add_segment()

    def add_segment(self):
        t = Turtle()
        if len(self.tail) == 0:
            prev = self.head
        else:
            prev = self.tail[-1]
        t.pu()
        t.setheading(prev.heading())
        t.shape("square")
        t.color(self.color)
        if t.heading() == 0:
            x = prev.xcor() - self.segment_size
            y = prev.ycor()
        elif t.heading() == 90:
            x = prev.xcor()
            y = prev.ycor() - self.segment_size
        elif t.heading() == 180:
            x = prev.xcor() + self.segment_size
            y = prev.ycor()
        elif t.heading() == 270:
            x = prev.xcor()
            y = prev.ycor() + self.segment_size
        t.goto(x, y)
        self.tail.append(t)

    def move(self):
        prev_positions = [(self.head.xcor(), self.head.ycor())]
        prev_headings = [self.head.heading()]
        for t in self.tail[:-1]:
            prev_positions.append((t.xcor(), t.ycor()))
            prev_headings.append(t.heading())

        for i in range(len(self.tail)):
            self.tail[i].goto(prev_positions[i])
            self.tail[i].setheading(prev_headings[i])
        self.head.fd(self.segment_size)

    def up(self):
        if int(self.head.xcor()) != int(self.tail[0].xcor()):
            self.head.setheading(UP)

    def down(self):
        if int(self.head.xcor()) != int(self.tail[0].xcor()):
            self.head.setheading(DOWN)

    def left(self):
        if int(self.head.ycor()) != int(self.tail[0].ycor()):
            self.head.setheading(LEFT)

    def right(self):
        if int(self.head.ycor()) != int(self.tail[0].ycor()):
            self.head.setheading(RIGHT)

    def change_color(self, color):
        self.color = color
        self.head.color(color)
        for t in self.tail:
            t.color(color)

    def reset(self):

        for t in self.tail:
            t.goto(1000, 1000)

        self.head.goto(0,0)
        self.head.setheading(0)
        self.tail = []
        for i in range(2):
            self.add_segment()
            self.tail[-1].goto(-self.segment_size*(i+1), 0)