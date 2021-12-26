import time
import turtle
from math import*
wn = turtle.Screen()
wn.setup(500,500)
wn.title("Perihelion precesssion of Mercury")
wn.tracer(0)
s = turtle.Turtle()
m = turtle.Turtle()
m_f = turtle.Turtle()
s.hideturtle()
m.hideturtle()
m_f.hideturtle()
m_f.color("cyan")
r_sun = 40
r_m = 15
xt = 50
s.pu()
s.fd(r_sun)
s.left(90)
s.pd()
s.circle(r_sun)
list = []
# for i in range(361):
#     A = radians(i)
#     x = 1.5*100*cos(A)
#     y = 100*sin(A)
#     point = turtle.Vec2D(x,y)
#     list.append(point)
def C(tur):
    tur.pu()
    tur.fd(5)
    tur.pd()
    tur.left(90)
    tur.circle(5)
    tur.right(90)
    tur.pu()
    tur.bk(5)

for i in range(180,-181,-1):
    A = radians(-i)
    x = 1.5*100*cos(A)
    y = 100*sin(A)
    point = turtle.Vec2D(x+xt, y)
    list.append(point)
# for i in range(30):
#     newlist = []
#     for P in list:
#         new_p = P.rotate(12*i)
#         newlist.append(new_p)
#     for np in newlist:
#         if newlist.index(np)==0:
#             m.pu()
#             m.goto(np)
#             m.pd()
#         else:
#             m.goto(np)
for i in range(45):
    newlist = []
    for P in list:
        new_p = P.rotate(8*i)
        newlist.append(new_p)
    for np in newlist:
        if newlist.index(np)==0:
            m.pu()
            m_f.pu()
            m.goto(np)
            m_f.goto(np)
            C(m)
            wn.update()
            m.clear()
            m_f.pd()
        else:
            m.goto(np)
            m_f.goto(np)
            C(m)
            wn.update()
            m.clear()
        time.sleep(0.01)

turtle.done()

