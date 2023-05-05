def rect(turt, width, x, y):
    turt.up()
    turt.goto(x, y)
    turt.down()
    for i in range(2):
        turt.fd(width)
        turt.rt(90)
        turt.fd(width / 2)
        turt.rt(90)


def spiral(turt):  # простая спираль
    line = 2
    for i in range(360):
        turt.fd(line)
        turt.rt(10)
        line += 0.05


def spider(turt, legs, length):
    turt.lt(90)
    for i in range(legs):
        turt.fd(length)
        turt.fd(-length)
        turt.rt(360 / legs)

def line(turt, length, q):
    turt.lt(90)
    for i in range(q):
        turt.fd(length)
        turt.bk(length)
        turt.rt(90)
        turt.up()
        turt.fd(length * 0.15)
        turt.down()
        turt.lt(90)

def spiral_v2(turt, radius):  # TODO: FIX ME up
    import math
    angle = 0
    step = 2 * math.pi / 100
    while angle < 100 * 2 * math.pi:
        # увеличивать радиус круга и угол поворота черепашки
        radius += step
        angle += 10

        # переместить черепашку в нужные координаты для рисования
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        turt.goto(x, y)


def tri_spiral(turt, length):
    for i in range(360):
        turt.fd(length)
        turt.lt(120)
        length += 5



