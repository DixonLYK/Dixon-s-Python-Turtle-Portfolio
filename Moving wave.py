import time
import turtle
from math import*
wn = turtle.Screen()
wn.tracer(0)
p = turtle.Turtle()
s = turtle.Turtle()
t = turtle.Turtle()
s.hideturtle()
p.hideturtle()
# t.hideturtle()
t.setheading(270)
t.color("black","yellow")
r = 5
def C():
    # tu.pu()
    t.fd(5)
    t.left(90)
    t.pd()
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.pu()
    t.right(90)
    t.bk(5)

p.pu()
s.pu()
p.goto(-180,0)
s.goto(p.pos())
s.pd()
s.left(90)
s.fd(180)
for i in range(3):
    s.right(90)
    s.fd(360)
s.right(90)
s.fd(180)
x = p.xcor()
p.pd()
offset = 0
t.pu()
while True:
    offset+=1
    for i in range(361):
        a = radians(i)
        if i == 0:
            p.pu()
            p.goto(x + 1, 100 * sin(a - radians(offset)))
            p.pd()
        else:
            p.goto(x + 1, 100 * sin(a - radians(offset)))
        x = p.xcor()
        t.goto(0,100*sin(pi - radians(offset)))
        # t.dot(5)
    wn.update()
    time.sleep(0.001)
    p.clear()
    t.clear()
    p.pu()
    p.goto(-180,0)
    x = p.xcor()
turtle.done()
