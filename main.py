import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Hamma the snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Detect collision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.new_location()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
