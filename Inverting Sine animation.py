import time
from math import *
import turtle
wn =turtle.Screen()
wn.tracer(0)
t = turtle.Turtle()
t.hideturtle()
t.pu()
t.goto(-180,0)
t.pd()

while True:
    for k in range(10,-11,-1):
        t.clear()
        for i in range(-180,181):
            t.goto(i,-(k/10)*100*sin(radians(i)))
        t.pu()
        t.goto(-180,0)
        t.pd()
        wn.update()
        time.sleep(0.04) #0.04
    for k in range(10,-11,-1):
        t.clear()
        for i in range(-180,181):
            t.goto(i,(k/10)*100*sin(radians(i)))
        t.pu()
        t.goto(-180,0)
        t.pd()
        wn.update()
        time.sleep(0.04)


turtle.done()