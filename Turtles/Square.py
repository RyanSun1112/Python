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

# side_length = 1366 / 2 = 683
# side_length2 = 768 / 2 = 384



def draw_rectangle():
    t.penup()
    t.goto(-680,350)
    t.pendown()
    t.goto(674,350)
    t.goto(674,-343)
    t.goto(-680,-343)
    t.goto(-680,350)
# t.fd(side_length)
# t.rt(90)
# t.fd(side_length2)
# t.rt(90)
# t.fd(side_length)
# t.rt(90)
# t.fd(side_length2)
# t.rt(90)

def draw_square():
    global side_length
    side_length = random.randint(1,100)
    for i in range(4):
        t.fd(side_length)   # Forward: pixels
        t.rt(90)            # Right Turn: degree      

side_length = 0
# draw_rectangle()
import random
for i in range(400):
    t.penup()
    t.goto(random.randint(-680,670),random.randint(-680,350))
    t.pendown()
    draw_square()
    




turtle.done()
