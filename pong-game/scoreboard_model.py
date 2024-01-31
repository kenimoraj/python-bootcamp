from turtle import Turtle

FONT = ('Arial', 24, 'bold')
TOP_MARGIN = 40
RADIUS = 50

class Scoreboard:

    def __init__(self, pitch_width, pitch_height):
        self.left_turtle = Turtle()
        self.right_turtle = Turtle()

        for s in [self.left_turtle, self.right_turtle]:
            s.color("white")
            s.ht()
            s.penup()
            s.goto(0, pitch_height/2-TOP_MARGIN)


        self.score_left = 0
        self.score_right = 0
        
        self.left_turtle.goto(-RADIUS, self.left_turtle.ycor())
        self.right_turtle.goto(RADIUS, self.left_turtle.ycor())
        self.left_turtle.write(self.score_left, move=False, align="center", font=FONT)
        self.right_turtle.write(self.score_right, move=False, align="center", font=FONT)


    def increase_score_left(self):
        self.score_left += 1
        self.left_turtle.clear()
        self.left_turtle.write(self.score_left, move=False, align="center", font=FONT)

    def increase_score_right(self):
        self.score_right += 1
        self.right_turtle.clear()
        self.right_turtle.write(self.score_right, move=False, align="center", font=FONT)