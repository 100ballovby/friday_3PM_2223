from turtle import *


t = Turtle()
screen = Screen()  # экран для черепашки
screen.setup(width=1280, height=720)
screen.addshape('3d-rocket.gif')
t.shape('3d-rocket.gif')
screen.bgpic('bg.gif')


move_speed = 10
turn_speed = 10

def forward():
    t.fd(move_speed)
def backward():
    t.bk(move_speed)
def left():
    t.lt(turn_speed)
def right():
    t.rt(turn_speed)

t.speed(0)
t.up()
t.home()

# связываем работу функций с кнопками на клавиатуре
screen.onkey(forward, 'Up')
screen.onkey(backward, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.listen()

done()
