from turtle import Turtle, Screen
import random


timmy = Turtle()
screen = Screen()
screen.colormode(255)



def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def background_color():
    screen.bgcolor(random_color())

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    timmy.color(random_color())

def penup():
    timmy.penup()

def pendown():
    timmy.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="q", fun=penup)
screen.onkey(key="r", fun=pendown)
screen.onkey(key="b", fun=background_color)
screen.exitonclick()
