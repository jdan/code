import turtle
from math import *

def trace(loc = 'output.path'):
    f = open(loc,'r')
    cx = 0
    cy = 0
    ctheta = 0

    turtle.down()

    for line in f.readlines():
        x = float(line.split(',')[0])
        y = float(line.split(',')[1])
    ##    dx = x - cx
    ##    dy = y - cx
    ##    dist = sqrt(dx ** 2 + dy ** 2)
    ##    theta = atan(dy / dx)
    ##    turtle.right((theta - ctheta) * (180/pi))
    ##    turtle.forward(dist)
    ##    cx = x
    ##    cy = y
    ##    ctheta = theta
        turtle.goto(x, y)
        
    f.close()
    
