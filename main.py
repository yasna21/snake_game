from turtle import Turtle, Screen
from snake_class import Snake
import time
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.tracer(0)

snake = Snake()

scoreboard = ScoreBoard()

food = Food()
screen.listen()
screen.onkey(key="Up", fun= snake.Up)
screen.onkey(key="Down", fun=snake.Down)
screen.onkey(key="Right", fun=snake.Right)
screen.onkey(key="Left", fun=snake.Left)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 297 or snake.head.xcor() < -297 or snake.head.ycor() > 297 or snake.head.ycor() < -297:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.segments[1: ]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()





















screen.exitonclick()