from turtle import *
import random

def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def showflakeArm():
    for x in range(0, 4):
        forward(30)
        vshape()
    backward(120)

def showflake():
    for x in range(0,10):
        showflakeArm()
        right(36)

color("red")
shape("turtle")
speed(10)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")


showflake()