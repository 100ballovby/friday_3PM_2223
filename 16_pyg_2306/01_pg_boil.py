import pygame as pg
import random as r


# Здесь определяются константы, классы и функции
FPS = 60
H = 720
W = 1280
MAGENTA = (255, 28, 111)
LIGHT_GREEN = (237, 255, 191)
BLUE = (45, 136, 189)


def generate_blocks():
    line = pg.sprite.Group()
    for row in range(5):
        for column in range(8):
            brick = pg.Surface((60, 20))
            brick.fill(BLUE)
            rect = brick.get_rect()
            rect.x = 75 * column + 10
            rect.y = 30 * row
    return line


# здесь создаем и инициализируем объекты для игры
pg.init()
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

player = pg.Rect(W / 2, H / 2, 50, 50)  # создаем на экране место под игровой объект
player.center = W // 2, H // 2
paddle = pg.Rect(W / 2, H - 30, 150, 30)  # создаем на экране место под ракетку
paddle.center = W // 2, H - 30

speed = 7
speed_x = speed_y = speed
player_moving = False
motion = 'STOP'


# до начала работы обновляем экран игры
pg.display.update()

while True:
    # FPS
    clock.tick(FPS)

    # цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_moving = True
                motion = 'LEFT'
            elif event.key == pg.K_RIGHT:
                player_moving = True
                motion = 'RIGHT'
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player_moving = False
                motion = 'STOP'
            elif event.key == pg.K_RIGHT:
                player_moving = False
                motion = 'STOP'

    # изменение объектов игры
    screen.fill(LIGHT_GREEN)
    pg.draw.ellipse(screen, MAGENTA, player)
    pg.draw.rect(screen, BLUE, paddle)

    bricks = generate_blocks()
    for i in range(len(bricks)):
        red = r.randint(0, 255)
        green = r.randint(0, 255)
        blue = r.randint(0, 255)
        pg.draw.rect(screen, (red, green, blue), bricks[i])

    # обновляем экран (это всегда должно находиться внизу)
    pg.display.update()

    player.x += speed_x
    player.y += speed_y

    if player.top <= 0 or player.bottom >= H:
        speed_y *= -1
    elif player.left <= 0 or player.right >= W:
        speed_x *= -1
    elif player.colliderect(paddle):  # если столкнулись с платформой
        speed_x *= -1
        speed_y *= -1

    if player_moving and motion == 'LEFT':
        paddle.x -= speed
    elif player_moving and motion == 'RIGHT':
        paddle.x += speed

