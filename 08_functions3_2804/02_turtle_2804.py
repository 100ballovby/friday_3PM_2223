from turtle import *
from turt_f import square, make_color, triangle   # из файла turt_f.py импортировать функцию square


t = Turtle()  # создание точки входа в программу
t.shape('turtle')

x = -200
side = 60
for i in range(3):
    c = make_color()
    square(t, x, 100, side, c)
    triangle(t, x, 100, side, c)
    x += side + 5


t.up()
t.goto(0, 0)
t.down()

t.circle(50)  # окружность рисуется ИЗ НИЖНЕЙ ТОЧКИ
t.dot(100)  # круг рисуется ИЗ ЦЕНТРА

done()  # чтобы окно не закрывалось сразу после начала работы
