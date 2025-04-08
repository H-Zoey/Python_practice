#DAY16
'''
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

print(table.align)
table.align = "l"
print(table.align)
print(table)'
'''



#DAY18
'''
import  turtle as t
import random

direction = [0, 90, 180, 270]

tim = t.Turtle()
t.colormode(255)
tim.width(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)    
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_shape(side_number):
    angle = 360 / side_number
    for i in range(side_number):
        tim.forward(100)
        tim.right(angle)

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(60)

screen = t.Screen()
screen.exitonclick()
'''



#DAY19 the turtle game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the game? Enter a color:")


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-150, -100, -50, 0, 50, 100]

all_turtles = []
for turtle_index in range(0, 6):
    turtle = Turtle(shape = "turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x = -240, y = y_position[turtle_index])
    all_turtles.append(turtle)
    
is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} is the winner!")
            else:
                print(f"You lose! The {winning_color} is the winner!")
        forward_distance = random.randint(0, 10)
        turtle.forward(forward_distance)

screen.exitonclick()