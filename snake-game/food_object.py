from turtle import Turtle
from random import randint
from snake_game_constants import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SEGMENT_SIZE, SNAKE_INITIAL_LENGTH, FOOD_SIZE

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.turtlesize(FOOD_SIZE)
        self.set_random_color()
        self.pu()

        self.refresh()

    def refresh(self):

        position_increment = SNAKE_SEGMENT_SIZE
        limitx = int(SCREEN_WIDTH/(2*position_increment))-1
        limity = int(SCREEN_HEIGHT/(2*position_increment))-1
        x = randint(-limitx, limitx)*position_increment
        y = randint(-limity, limity)*position_increment

        self.set_random_color()
        self.goto(x, y)

    def set_random_color(self):
        r = randint(0, 1)
        g = randint(0, 1)
        b = randint(0, 1)
        while (r, g, b) == (0, 0, 0):
            r = randint(0, 1)
            g = randint(0, 1)
            b = randint(0, 1)

        self.color((r, g, b))