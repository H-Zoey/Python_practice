#Day20 the snake game
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)#不自动刷新

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()#update manually
    time.sleep(0.1)#update several segments samely

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_increase()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #detect collision with tail - if head collides any segment in the tail, game over will be triggered.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

        

    snake.move()
    


        












screen.exitonclick()
