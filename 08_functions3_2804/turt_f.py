"""
в этом файле находятся функции, которые позволяют черепашке рисовать различные фигуры
"""
import random as r


def square(turt, x, y, length, color='black'):
    turt.up()  # поднять перо (перестать рисовать)
    turt.goto(x, y)  # перейти в координаты x, y (задано в параметрах)
    turt.down()  # опустить перо (начать рисовать)
    turt.color(color)  # установить цвет из параметра
    for i in range(4):
        turt.fd(length)  # идти вперед на length шагов
        turt.rt(90)  # поворачивать вправо на 90 градусов


def triangle(turt, x, y, length, color='black'):
    turt.up()  # поднять перо (перестать рисовать)
    turt.goto(x, y)  # перейти в координаты x, y (задано в параметрах)
    turt.down()  # опустить перо (начать рисовать)
    turt.color(color)  # установить цвет из параметра
    for i in range(3):
        turt.fd(length)  # идти вперед на length шагов
        turt.lt(120)  # поворачивать вправо на 90 градусов

def make_color():
    alphabet = 'abcdef0123456789'  # алфавит шестнадцатеричной системы счисления
    color = '#'  # решетка стоит в начале цвета в HEX-модели
    for i in range(6):  # повторить 6 раз (потому что количество символов в коде - 6)
        r_index = r.randint(0, len(alphabet) - 1)  # сгенерировать случайный индекс из алфавита
        color += alphabet[r_index]  # забрать символ по случайному индексу и добавить его к цвету
    return color




