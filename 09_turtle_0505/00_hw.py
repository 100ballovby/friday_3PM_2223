from turtle import *


def x_angle(turt, angles, length, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    angle = 360 / angles
    for i in range(angles):
        turt.fd(length)
        turt.lt(angle)


t = Turtle()

x_angle(t, 4, 100, 100, 100)
x_angle(t, 3, 100, -100, -100)
x_angle(t, 6, 100, 20, 20)
x_angle(t, 12, 50, 200, 200)
x_angle(t, 5, 50, -200, -200)

done()


