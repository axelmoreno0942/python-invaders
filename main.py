import pygame as pg
from pygame.locals import *
pg.init()

running = True

screen = pg.display.set_mode((480,640))
pg.display.set_caption("McInvaders")

bg = pg.image.load('Assets/fond.png')
bg = pg.transform.scale(bg, screen.get_size())


clock = pg.time.Clock()

direction = True

velocity = 12
x = 190

ship = pg.image.load('Assets/spritesheets/shipOP.png')
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
    clock.tick(60)
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            quit()
 
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                direction = True
            elif event.key == pg.K_LEFT:
                direction = False
 
    key_pressed_is = pg.key.get_pressed()
    if event.type==KEYDOWN:
        if key_pressed_is[K_LEFT]:
            x -= velocity
        if key_pressed_is[K_RIGHT]:
            x += velocity
 
    screen.blit(bg,(0,0))
 
    image =  pg.transform.scale((pg.image.load('Assets/spritesheets/shipOP.png')),(96, 122))
    screen.blit(image, (x,500))
    
    pg.display.update()

pg.quit()