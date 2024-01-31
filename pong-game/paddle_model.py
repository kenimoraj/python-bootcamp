import turtle
from turtle import Turtle

PADDLE_COLOR = "white"
PADDLE_SEGMENTS_N = 6
PADDLE_SCALE = 0.5
PADDLE_SEGMENT_SIZE = 20*PADDLE_SCALE
PADDLE_MOVE_INCREMENT = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color(PADDLE_COLOR)

        self.thickness = PADDLE_SEGMENT_SIZE

        self.upper_wing = []
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_SCALE, stretch_len=PADDLE_SCALE*PADDLE_SEGMENTS_N)
        self.penup()


    def distance(self, object):

        #distances from segments
        dist = []
        for i in range(-int(PADDLE_SEGMENTS_N/2), int(PADDLE_SEGMENTS_N/2)):
            dist.append(object.distance(self.xcor(),self.ycor()+i*PADDLE_SEGMENT_SIZE))

        return min(dist)

    def up(self):
        x = self.xcor()
        y = self.ycor() + PADDLE_MOVE_INCREMENT
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - PADDLE_MOVE_INCREMENT
        self.goto(x, y)