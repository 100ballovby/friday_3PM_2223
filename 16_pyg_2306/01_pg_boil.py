import pygame as pg
import random as r


# Здесь определяются константы, классы и функции
FPS = 60
H = 480
W = 640
MAGENTA = (255, 28, 111)
LIGHT_GREEN = (237, 255, 191)
BLUE = (45, 136, 189)


def paddle_motion(pl, s_w):
    if pl.right >= s_w:
        pl.right = s_w
    elif pl.left <= 0:
        pl.left = 0

# здесь создаем и инициализируем объекты для игры
pg.init()
pg.mixer.init()
pg.font.init()

font_text = pg.font.SysFont('comicsans', 24)

hit_sound = pg.mixer.Sound('hit.mp3')  # загрузка звукового файла
hit_sound.set_volume(0.4)  # громкость проигрывания звукового файла
lose_sound = pg.mixer.Sound('lose.wav')
lose_sound.set_volume(0.3)

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

ball_img = pg.image.load('tennis.png').convert_alpha()
ball_img = pg.transform.scale(ball_img, (70, 70))

player = ball_img.get_rect()  # создаем на экране место под игровой объект
player.center = W // 2, H // 2
paddle = pg.Rect(W / 2, H - 30, 150, 30)  # создаем на экране место под ракетку
paddle.center = W // 2, H - 30

speed = 7
speed_x = speed_y = speed
player_moving = False
motion = 'STOP'


# до начала работы обновляем экран игры
pg.display.update()

game_over = False
while True:
    while game_over:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    player.center = W // 2, H // 2
                    game_over = False
                if event.key == pg.K_q:
                    exit()
        screen.fill(LIGHT_GREEN)
        the_end = font_text.render("C - is for continue,Q - is for quit", True, (0, 0, 0))
        screen.blit(the_end, (20, H // 2))
        pg.display.update()
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
    screen.blit(ball_img, player)
    pg.draw.rect(screen, BLUE, paddle)

    # обновляем экран (это всегда должно находиться внизу)
    pg.display.update()

    player.x += speed_x
    player.y += speed_y

    if player.top <= 0:
        speed_y *= -1
        pg.mixer.Sound.play(hit_sound)
    elif player.bottom >= H:
        pg.mixer.Sound.play(lose_sound)
        game_over = True
    elif player.left <= 0 or player.right >= W:
        speed_x *= -1
        pg.mixer.Sound.play(hit_sound)
    elif player.colliderect(paddle):  # если столкнулись с платформой
        speed_x *= -1
        speed_y *= -1
        pg.mixer.Sound.play(hit_sound)

    paddle_motion(paddle, W)

    if player_moving and motion == 'LEFT':
        paddle.x -= speed
    elif player_moving and motion == 'RIGHT':
        paddle.x += speed

