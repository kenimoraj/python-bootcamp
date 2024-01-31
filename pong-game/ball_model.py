from turtle import Turtle
from random import randint


SCALE = 0.5
BALL_COLOR = "white"
BALL_INITIAL_SPEED = 10
BALL_SIZE = 20*SCALE


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.shapesize(stretch_wid=SCALE, stretch_len=SCALE)

        self.direction = 0
        self.set_rand_direction()
        self.ball_speed = BALL_INITIAL_SPEED
        self.penup()


    def move(self):
        self.setheading(self.direction)
        self.fd(self.ball_speed)

    def bounce_y(self):
        self.direction = (-self.direction) % 360
    def bounce_x(self):
        self.direction = (180 - self.direction) % 360
        # if self.direction//90 in [0, 2]:
        #     self.direction = (180 - self.direction) % 360
        # else:
        #     self.direction = (self.direction - 90) % 360

    def getsize(self):
        return BALL_SIZE

    def setspeed(self, speed):
        self.ball_speed = speed

    def set_rand_direction(self):
        self.direction = randint(-45, 45) + randint(0, 1)*180