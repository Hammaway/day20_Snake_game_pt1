import time
from turtle import Screen, Turtle
import timer

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Hamma the snake")
screen.tracer(0)

snake_list = []
starting_x = 0
for i in range(3):
    new_square = Turtle()
    new_square.shape('square')
    new_square.color('white')
    new_square.penup()
    new_square.goto(starting_x, 0)
    starting_x -= 20
    snake_list.append(new_square)
screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()
