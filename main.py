import pygame as pg
pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("McInvaders")

bg = pg.image.load('Assets/bg.jpeg')

ship = pg.image.load('Assets/spritesheets/shipOP.png')
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

screen.blit(ship, (ship_left,ship_top))

MenuButton = pg.image.load('Assets/buttons/MENU.png').convert_alpha()
PauseButton = pg.image.load('Assets/buttons/PAUSE.png').convert_alpha()
PlayButton = pg.image.load('Assets/buttons/PLAY.png').convert_alpha()
QuitButton = pg.image.load('Assets/buttons/QUIT.png').convert_alpha()
CrossButton = pg.image.load('Assets/buttons/x.png').convert_alpha()
ResumeButton = pg.image.load('Assets/buttons/RESUME.png').convert_alpha()
Logo = pg.image.load('Assets/logo.png').convert_alpha()

x = 220
y = 520
width = 40
height = 60
vel = 5

run = True

while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= vel
    if keys[pg.K_RIGHT]:
        x += vel
    
    screen.fill()
    pg.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()