from turtle import Turtle
from enum import IntEnum

STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10


class DIRECTION(IntEnum):
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for pos in STARTING_COORDINATES:
            self.add_segment(pos)

    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.snake_list.append(new_square)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self, direction=None):
        for i in range(len(self.snake_list) - 1, 0, -1):
            self.snake_list[i].goto(self.snake_list[i - 1].xcor(), self.snake_list[i - 1].ycor())
        if direction is not None:
            self.head.setheading(direction)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DIRECTION.DOWN:
            self.head.setheading(DIRECTION.UP)

    def move_down(self):
        if self.head.heading() != DIRECTION.UP:
            self.head.setheading(DIRECTION.DOWN)

    def move_left(self):
        if self.head.heading() != DIRECTION.RIGHT:
            self.head.setheading(DIRECTION.LEFT)

    def move_right(self):
        if self.head.heading() != DIRECTION.LEFT:
            self.head.setheading(DIRECTION.RIGHT)