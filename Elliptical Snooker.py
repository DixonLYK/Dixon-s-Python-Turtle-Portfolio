import time
import random
import turtle
from math import *
wn = turtle.Screen()
wn.title("Elliptical snooker table")
wn.tracer(0)
tb = turtle.Turtle()
ball = turtle.Turtle()
hole = turtle.Turtle()
trc = turtle.Turtle()
trc.color("yellow")

tb.hideturtle()
hole.hideturtle()
ball.hideturtle()
trc.hideturtle()


def C(r,tu,ol,clr):
    tu.color(ol,clr)
    tu.pu()
    tu.fd(r)
    tu.left(90)
    tu.pd()
    tu.begin_fill()
    tu.circle(r)
    tu.end_fill()
    tu.pu()
    tu.right(90)
    tu.bk(r)

border_pts = []
ell_pts = []

for i in range(210,-211,-1):
    y = 160*(sqrt(1-(i/210)**2))
    border_pts.append(turtle.Vec2D(i,y))
for i in range(-210,211):
    y = -160 * (sqrt(1 - (i / 210) ** 2))
    border_pts.append(turtle.Vec2D(i, y))
tb.pu()
tb.goto(210,0)
tb.pd()

tb.color("black","#31D82B")
tb.begin_fill()
for pt in border_pts:
    tb.goto(pt)
tb.end_fill()


for i in range(200,-201,-1):
    y = 150*(sqrt(1-(i/200)**2))
    ell_pts.append(turtle.Vec2D(i,y))
for i in range(-200,201):
    y = -150 * (sqrt(1 - (i / 200) ** 2))
    ell_pts.append(turtle.Vec2D(i, y))

tb.pu()
tb.goto(200,0)
tb.pd()

tb.color("black","#31D82B")
tb.begin_fill()
for pt in ell_pts:
    tb.goto(pt)
tb.end_fill()


c = sqrt(200**2 - 150**2)
ball.goto(c,0)
C(5,ball,"black","white")

trc.pu()
trc.goto(ball.pos())
trc.pd()

hole.goto(-c,0)
C(10,hole,"black","black")


x = ball.xcor()
y = ball.ycor()

while True:
    ball.setheading(random.randint(0, 360))
    x = ball.xcor()
    y = ball.ycor()
    trc.pd()

    while (x+c)**2+y**2 > 8**2:
        ball.clear()
        ball.fd(2)
        trc.goto(ball.pos())
        C(5, ball, "black", "white")
        x = ball.xcor()
        y = ball.ycor()
        if (x / 195) ** 2 + (y / 145) ** 2 > 1:
            th = ball.heading() - degrees(atan((1521*y)/(841*x)))
            alph = 180 - 2 * th
            ball.left(alph)
            ball.fd(1)
            trc.goto(ball.pos())
            ball.pd()
            C(5, ball, "black", "white")
            x = ball.xcor()
            y = ball.ycor()

        wn.update()
        time.sleep(0.001)
    ball.clear()
    ball.pu()
    trc.pu()
    ball.goto(c,0)
    trc.goto(ball.pos())
    wn.update()
turtle.done()
