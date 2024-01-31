from turtle import Turtle,Screen
from paddle_model import Paddle
from ball_model import Ball, BALL_INITIAL_SPEED
from scoreboard_model import Scoreboard
from time import sleep
from math import fabs

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = "black"
PADDLE_MARGIN = 20

PITCH_HEIGHT = SCREEN_HEIGHT-200
PITCH_WIDTH = SCREEN_WIDTH-100

FRAME = 0.02
TIME_BETWEEN_ROUNDS = 1

BALL_SPEED_INCREMENT = 2

def draw_pitch():
    h = PITCH_HEIGHT
    w = PITCH_WIDTH
    t = Turtle()
    t.ht()
    t.pensize(5)
    t.color("white")
    t.penup()
    t.lt(90)
    t.bk(h/2)
    t.rt(90)
    t.bk(w/2)
    t.lt(90)
    t.pendown()
    for _ in range(2):
        t.fd(h)
        t.rt(90)
        t.fd(w)
        t.rt(90)
    t.pu()

    t.home()
    t.pd()
    t.pensize(2)
    t.lt(90)
    t.fd(PITCH_HEIGHT/2)
    t.bk(PITCH_HEIGHT)
    t.fd(PITCH_HEIGHT/2)
    t.pu()

def setup_paddles():
    paddle_left = Paddle()
    paddle_right = Paddle()
    paddle_left.goto(-(PITCH_WIDTH/2-PADDLE_MARGIN), 0)
    paddle_left.setheading(90)
    paddle_right.goto((PITCH_WIDTH/2-PADDLE_MARGIN), 0)
    paddle_right.setheading(90)

    return (paddle_left, paddle_right)


def wall_bounce(ball):

    if fabs(ball.ycor()) > PITCH_HEIGHT/2 - ball.getsize()/2:
        ball.bounce_y()
        while fabs(ball.ycor()) > PITCH_HEIGHT/2 - ball.getsize()/2:
            ball.move()

    if fabs(ball.xcor()) > PITCH_WIDTH/2:
        if ball.xcor() > 0:
            scoreboard.increase_score_left()
        else:
            scoreboard.increase_score_right()
        ball.goto(0, 0)
        ball.setspeed(BALL_INITIAL_SPEED)
        for p in [paddle_left, paddle_right]:
            p.goto(p.xcor(), 0)
        screen.update()
        ball.set_rand_direction()
        sleep(TIME_BETWEEN_ROUNDS)

        # while fabs(ball.xcor()) > PITCH_WIDTH / 2 - ball.getsize() / 2:
        #     ball.move()


def paddle_bounce(ball, paddle1, paddle2):
    for paddle in [paddle1, paddle2]:
        if paddle.distance(ball) < 10:
            ball.bounce_x()
            while paddle.distance(ball) < 10:
                ball.move()
            ball.setspeed(ball.ball_speed + BALL_SPEED_INCREMENT)




screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("SPIERDALAJ")
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(False)

(paddle_left, paddle_right) = setup_paddles()
ball = Ball()
draw_pitch()
scoreboard = Scoreboard(PITCH_WIDTH, PITCH_HEIGHT)
screen.update()
screen.listen()

screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")

while True:
    ball.move()
    
    screen.update()
    sleep(FRAME)
    wall_bounce(ball)
    paddle_bounce(ball, paddle_left, paddle_right)
screen.exitonclick()
