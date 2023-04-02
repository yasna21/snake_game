from turtle import Turtle, Screen
import time
POSSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in POSSITION_LIST:
            self.add_segments(position)


    def add_segments(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.segments.append(square)


    def extend(self):
        self.add_segments(self.segments[-1].position())



    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






    def move(self):


            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)
