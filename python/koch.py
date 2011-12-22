from turtle import *
from math import sqrt

def draw_edge(t, dist, max_r = 1):
    if not max_r:
        t.forward(dist)
        t.left(60)
        t.forward(dist)
        t.right(120)
        t.forward(dist)
        t.left(60)
        t.forward(dist)
    else:
        draw_edge(t, dist / 3, max_r - 1)
        t.left(60)
        draw_edge(t, dist / 3, max_r - 1)
        t.right(120)
        draw_edge(t, dist / 3, max_r - 1)
        t.left(60)
        draw_edge(t, dist / 3, max_r - 1)

def main():
    dist = 81
    depth = 4
    
    t = Turtle()
    t.speed(50000)
    
    for a in range(0, 3):
        draw_edge(t, dist, depth)
        t.right(120)
        
    while 1:
        pass
    
if __name__ == '__main__':
    main()