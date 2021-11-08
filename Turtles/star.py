import turtle
from random import randint
# Set the background color
screen = turtle.Screen()
screen.bgcolor('white')   # black
# Create a turtle
t = turtle.Turtle()
t.width(2)
t.color('red')
t.speed(100)

side_length= 300
for i in range(6):
    t.fd(side_length)
    t.rt(144)

turtle.done()