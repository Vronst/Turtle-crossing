from turtle import Turtle

FONT = ("Courier", 24, "normal")
L_FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.n_lives = 3
        self.penup()
        self.hideturtle()
        self.score_up()
        self.lives()

    def score_up(self):
        self.goto(-100, 260)
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)
        self.lives()

    def reset_(self):
        self.n_lives -= 1
        self.score -= 1
        self.score_up()
        self.lives()

    def lives(self):
        self.goto(100, 260)
        self.write(arg=f"Lives: {self.n_lives}", align="center", font=L_FONT)

    def game_over(self):
        self.color("red")
        self.home()
        self.write(arg=f"Game over\nHighest level: {self.score}", align="center", font=FONT)
