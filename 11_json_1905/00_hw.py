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

def triangle(obj, x, y, col1, col2, width):
    obj.up()
    obj.goto(x, y)
    obj.down()
    obj.color(col1)  # цвет обводки
    obj.fillcolor(col2)  # цвет заливки

    obj.begin_fill()  # начать закрашивать
    for i in range(3):
        obj.fd(width)
        obj.lt(120)
    obj.end_fill()  # закончить закрашивать

def draw_house(obj, x, y, width):
    rect(obj, x, y, colors['brown'], colors['ohra'], width, width)
    triangle(obj, x - 10, y, colors['brown'], colors['orange'], width + 20)


rect(t, -s_width // 2, 0, colors['light_green'], colors['green'], s_width, s_height // 2)  # земля
rect(t, -s_width // 2, s_height // 2, colors['blue'], colors['blue'], s_width, s_height // 2)  # земля
house_x = -200
house_y = 50
house_width = 150
draw_house(t, house_x, house_y, house_width)
rect(t, house_x + house_width // 3, house_y - house_width * 0.25, colors['brown'], colors['blue'], 50, 50)

t.up()
t.goto(200, 200)
t.down()
t.color(colors['yellow'])
t.dot(100)

done()
