from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("green")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        self.goto(random.randint(-290, 280), random.randint(-290, 290))
