import pygame as pg
from pygame.locals import *
pg.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("McInvaders")

bg = pg.image.load('Assets/fond.png')
bg = pg.transform.scale(bg, screen.get_size())

clock = pg.time.Clock()
running = True

x = 190
speed = 250
direction = True


ship = pg.image.load('Assets/spritesheets/shipOP.png')
ship = pg.transform.scale(ship,(96, 122))

MenuButton = pg.image.load('Assets/buttons/MENU.png').convert_alpha()
PauseButton = pg.image.load('Assets/buttons/PAUSE.png').convert_alpha()
PlayButton = pg.image.load('Assets/buttons/PLAY.png').convert_alpha()
QuitButton = pg.image.load('Assets/buttons/QUIT.png').convert_alpha()
CrossButton = pg.image.load('Assets/buttons/x.png').convert_alpha()
ResumeButton = pg.image.load('Assets/buttons/RESUME.png').convert_alpha()
Logo = pg.image.load('Assets/logo.png').convert_alpha()

def projectile():
    pass

while running:
    dt = clock.tick(60) / 1000
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
 
    keys = pg.key.get_pressed()
    if keys[K_LEFT] and x>0:
        x -= speed * dt
        direction = False
    if keys[K_RIGHT] and x < 480-96:
        x += speed * dt
        direction = True
 
    screen.blit(bg,(0,0))
    screen.blit(ship, (x,480))
    pg.display.update()

pg.quit()