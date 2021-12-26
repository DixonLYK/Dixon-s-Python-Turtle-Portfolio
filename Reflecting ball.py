import time
import turtle
import random
from math import *
wn = turtle.Screen()
wn.setup(500, 500)
wn.tracer(0)
t = turtle.Turtle()
p = turtle.Turtle()
t.hideturtle()
p.hideturtle()
a_i = random.randint(0,360)
a2_i =random.randint(0,360)
x = t.xcor()
y = t.ycor()
a = p.xcor()
b = p.ycor()
t.setheading(a_i)
p.setheading(a2_i)
t.color("black","yellow")
def C(tur):
    tur.pu()
    tur.fd(25)
    tur.pd()
    tur.left(90)
    t.begin_fill()
    tur.circle(25)
    t.end_fill()
    tur.right(90)
    tur.pu()
    tur.bk(25)
    tur.pd()

while True:
    x = t.xcor()
    y = t.ycor()
    while abs(x) <=225 and abs(y) <= 225:
        t.pu()
        t.fd(2)
        C(t)
        wn.update()
        time.sleep(0.001)
        t.clear()
        x = t.xcor()
        y = t.ycor()
        hed = t.heading()
    else:
        if y > 225:
            hed = t.heading()
            t.pu()
            if 0<hed<=90:
                th = 90-hed
                t.right(180-2*th)
                t.fd(2)
                t.pd()
                C(t)
                wn.update()
            elif 90<hed<180:
                t.left(2*(180-hed))
                t.fd(2)
                t.pd()
                C(t)
                wn.update()
            wn.update()
        elif y<-225:
            hed = t.heading()
            t.pu()
            if 270<=hed<=360:
                th = hed-270
                alph = 180-2*th
                t.left(alph)
                t.fd(2)
                t.pd()
                wn.update()
            elif 180<=hed<270:
                th = 270-hed
                alph = 180-2*th
                t.right(alph)
                t.fd(2)
                t.pd()
                wn.update()
        elif x>225:
            hed = t.heading()
            t.pu()
            if 0<=hed<=90:
                alph = 180-2*hed
                t.left(alph)
                t.fd(2)
                t.pd()
                wn.update()
            elif 270<=hed<=360:
                th = 360 - hed
                alph = 180 - 2*th
                t.right(alph)
                t.fd(2)
                t.pd()
                wn.update()
        elif x<-225:
            hed = t.heading()
            t.pu()
            if 90<=hed<=180:
                th = 180-hed
                alph = 180 - 2*th
                t.right(alph)
                t.fd(2)
                t.pd()
                wn.update()
            elif 180<hed<=270:
                th = hed -180
                alph = 180 - 2*th
                t.left(alph)
                t.fd(2)
                t.pd()
                wn.update()
        ####################################################3
        # a = t.xcor()
        # b = t.ycor()
        # while abs(a) <= 225 and abs(b) <= 225:
        #     p.pu()
        #     p.fd(2)
        #     C(p)
        #     wn.update()
        #     time.sleep(0.001)
        #     p.clear()
        #     a = p.xcor()
        #     b = p.ycor()
        #     hed = p.heading()
        # else:
        #     if b > 225:
        #         hed = p.heading()
        #         p.pu()
        #         if 0 < hed <= 90:
        #             th = 90 - hed
        #             p.right(180 - 2 * th)
        #             p.fd(2)
        #             p.pd()
        #             C(p)
        #             wn.update()
        #         elif 90 < hed < 180:
        #             t.left(2 * (180 - hed))
        #             p.fd(2)
        #             p.pd()
        #             C(p)
        #             wn.update()
        #         wn.update()
        #     elif b < -225:
        #         hed = p.heading()
        #         p.pu()
        #         if 270 <= hed <= 360:
        #             th = hed - 270
        #             alph = 180 - 2 * th
        #             p.left(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        #         elif 180 <= hed < 270:
        #             th = 270 - hed
        #             alph = 180 - 2 * th
        #             p.right(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        #     elif a > 225:
        #         hed = p.heading()
        #         p.pu()
        #         if 0 <= hed <= 90:
        #             alph = 180 - 2 * hed
        #             p.left(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        #         elif 270 <= hed <= 360:
        #             th = 360 - hed
        #             alph = 180 - 2 * th
        #             p.right(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        #     elif a < -225:
        #         hed = p.heading()
        #         p.pu()
        #         if 90 <= hed <= 180:
        #             th = 180 - hed
        #             alph = 180 - 2 * th
        #             p.right(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        #         elif 180 < hed <= 270:
        #             th = hed - 180
        #             alph = 180 - 2 * th
        #             p.left(alph)
        #             p.fd(2)
        #             p.pd()
        #             wn.update()
        wn.update()
        continue







# while True:
#     x = t.xcor()
#     y = t.ycor()
#     ang = t.heading()
#     while abs(x) <=225 and abs(y) <=225:
#         if ang == 180:
#             t.pu()
#             t.fd(2)
#             t.pd()
#             t.circle(-25)
#             wn.update()
#             time.sleep(0.001)
#             t.clear()
#         else:
#             t.pu()
#             t.fd(2)
#             t.pd()
#             t.circle(25)
#             wn.update()
#             time.sleep(0.001)
#             t.clear()
#         x = t.xcor()
#         y = t.ycor()
#     else:
#         t.left(180)
#         t.pu()
#         t.fd(2)
#         t.pd()
#         t.circle(-25)
#         wn.update()
#
#         continue


turtle.done()