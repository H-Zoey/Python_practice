from turtle import Turtle
import random

class Food(Turtle):#class inheritance: class A(B)
    def __init__(self):
        super().__init__()#Food inherits parameters and functions of Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-280, 280)#height and width of the screen are 600, but it is too hard for the snake to get the edge(-300,300)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

