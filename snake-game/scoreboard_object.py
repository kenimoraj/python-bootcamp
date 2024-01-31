from turtle import Turtle
from snake_game_constants import SCREEN_HEIGHT

TOP_MARGIN = 50


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as hsfile:
            self.highscore = int(hsfile.read())
        self.reset()

    def write_score(self):
        self.pd()

        self.clear()
        self.write(f"Score: {self.score}  |  Highscore: {self.highscore}", align="center", font=("Arial", 20, "bold"))

        self.pu()

    def write_init(self):
        self.pd()

        self.clear()
        self.write("Press SPACE to start", align="center", font=("Arial", 20, "bold"))
        self.pu()

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as hsfile:
                hsfile.write(str(self.highscore))

    def game_over(self):
        self.pu()
        self.home()
        self.pd()
        self.write("GAME OVER", align="center", font=("Arial", 20, "bold"))
        self.pu()
        self.goto(0, SCREEN_HEIGHT/2-TOP_MARGIN)

    def reset(self):
        self.clear()
        self.goto(0,0)
        self.score = 0

        self.ht()
        self.penup()
        self.left(90)
        self.forward(SCREEN_HEIGHT / 2 - TOP_MARGIN)
        self.color("white")
        self.write_init()