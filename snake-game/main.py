import turtle
from turtle import Screen
from snake_object import Snake
from time import sleep
from food_object import Food
from scoreboard_object import Scoreboard
from snake_game_constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SEGMENT_SIZE, SNAKE_INITIAL_LENGTH, FOOD_SIZE

def draw_wall():
    t = snake.head
    orig_color = t.color()
    t.pensize(5)
    t.color("white")
    t.pu()
    t.lt(90)
    t.bk(SCREEN_HEIGHT/2-SNAKE_SEGMENT_SIZE/2)
    t.rt(90)
    t.bk(SCREEN_WIDTH/2 - SNAKE_SEGMENT_SIZE/2)
    t.lt(90)
    t.pd()
    for _ in range(2):
        t.fd(SCREEN_HEIGHT-SNAKE_SEGMENT_SIZE)
        t.rt(90)
        t.fd(SCREEN_WIDTH-SNAKE_SEGMENT_SIZE)
        t.rt(90)
    t.pu()
    t.color(orig_color[0])
    t.home()

def checkForCollisionWithFood():
    # print(f"({snake.head.xcor()},{food.xcor()})   ({snake.head.ycor()},{food.ycor()})")

    if int(snake.head.distance(food)) == 0:
        print(snake.head.distance(food))

        snake.change_color(food.fillcolor())
        snake.add_segment()
        food.refresh()


        scoreboard.increase_score()
        scoreboard.write_score()


def collisionWithWall():
    t = snake.head
    x = int(t.xcor())
    y = int(t.ycor())
    if x<0:
        x = -x
    if y<0:
        y = -y
    if x>=SCREEN_WIDTH/2 or y>=SCREEN_HEIGHT/2:
        return True
    else:
        return False

def collisionWithTail():
    h = snake.head
    tail = snake.tail

    for seg in tail:

        if int(h.xcor()) == int(seg.xcor()) and int(h.ycor()) == int(seg.ycor()):
            return True
    return False


def start_game():

    game_is_on = True
    scoreboard.write_score()
    while game_is_on:
        snake.move()
        screen.update()
        sleep(0.05)
        checkForCollisionWithFood()
        game_is_on = (not collisionWithWall()) and (not collisionWithTail())
    game_over()

def game_over():
    scoreboard.game_over()
    screen.onkey(reset_game, "space")

def reset_game():
    scoreboard.reset()
    snake.reset()
    screen.update()
    screen.onkey(start_game, "space")

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.listen()
screen.tracer(False)
snake = Snake(SNAKE_INITIAL_LENGTH, SNAKE_SEGMENT_SIZE, "pink")
food = Food()

scoreboard = Scoreboard()
draw_wall()
screen.update()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(start_game, "space")


screen.exitonclick()


