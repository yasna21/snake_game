from turtle import Turtle
from food import Food


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-55, 260)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game is Over!", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()








