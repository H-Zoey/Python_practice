#Day20 the snake game
from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)#不自动刷新

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()#手动刷新
    time.sleep(0.1)#使几个segment同时刷新

    snake.move()
    


        












screen.exitonclick()
