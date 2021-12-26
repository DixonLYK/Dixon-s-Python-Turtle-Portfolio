import time
import turtle
import random
from math import *
wn = turtle.Screen()
wn.title("Circular mirror")
wn.setup(500,500)
wn.tracer(0)
t = turtle.Turtle()
p = turtle.Turtle()
tu = turtle.Turtle()
t.hideturtle()
p.hideturtle()
tu.hideturtle()
tu.speed(0)
def C(r,tu):
    tu.color("black","yellow")
    tu.pu()
    tu.fd(r)
    tu.left(90)
    tu.pd()
    t.begin_fill()
    tu.circle(r)
    t.end_fill()
    tu.pu()
    tu.right(90)
    tu.bk(r)
r = 5
R =250
tu.pu()
tu.fd(R)
tu.left(90)
tu.pd()
tu.circle(R)
tu.pu()
tu.right(90)
tu.bk(R)

t.pu()
t.goto(random.randint(-100,100),random.randint(-100,100))
# t.goto(0,245*sin(radians(30)))
p.pu()
p.goto(t.pos())
t.setheading(random.randint(0,360))
x = t.xcor()
y = t.ycor()
p.pd()
while True:
    while x**2 + y**2 <= (250-r)**2:
        t.fd(1)
        p.goto(t.pos())
        t.pd()
        C(r,t)
        t.pu()
        x = t.xcor()
        y = t.ycor()
        wn.update()
        time.sleep(0.001)
        t.clear()
    else:
        th = t.heading()-degrees(atan(y/x))
        alph = 180 - 2*th
        t.left(alph)
        t.fd(1)
        p.goto(t.pos())
        t.pd()
        C(r, t)
        t.pu()
        x = t.xcor()
        y = t.ycor()
        wn.update()
        time.sleep(0.001)
        t.clear()
        continue


turtle.done()