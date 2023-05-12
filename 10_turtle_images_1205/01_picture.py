from turtle import *

t = Turtle()
sc = Screen()
s_width = 600
s_height = 600
sc.setup(s_width, s_height)
t.speed(0)
t.pensize(5)

colors = {
    'light_green': '#23f746',
    'green': '#02c923',
    'blue': '#94f8ff',
    'ohra': '#c4aa84',
    'red': '#db1424',
    'orange': '#db8114',
    'brown': '#593e1c',
    'yellow': '#f5ec8c',
    'marine': '#3c5c96',  # темно-синий
}


def rect(obj, x, y, color1, color2, width, height):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.color(color1)  # цвет обводки
    obj.fillcolor(color2)  # цвет заливки

    obj.begin_fill()  # начать закрашивать
    for i in range(2):
        obj.fd(width)
        obj.rt(90)
        obj.fd(height)
        obj.rt(90)
    obj.end_fill()  # закончить закрашивать


rect(t, -s_width // 2, 0, colors['light_green'], colors['green'], s_width, s_height // 2)  # земля
rect(t, -s_width // 2, s_height // 2, colors['blue'], colors['blue'], s_width, s_height // 2)  # земля

done()
