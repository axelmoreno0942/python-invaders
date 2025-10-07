import pygame as pg
from pygame.locals import *
import math

pg.init()

# Fenêtre
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("McInvaders")

# Fond
bg = pg.image.load('Assets/fond.png').convert()
bg = pg.transform.scale(bg, screen.get_size())
bg_height = bg.get_height()

scroll = 0
tiles = math.ceil(SCREEN_HEIGHT / bg_height) + 1

# Joueur
x = 190
speed = 250
direction = True

ship = pg.image.load('Assets/spritesheets/shipOP.png').convert_alpha()
ship = pg.transform.scale(ship, (96, 122))

laser = pg.image.load('Assets/spritesheets/cannon_ball.png').convert_alpha()

# Horloge
clock = pg.time.Clock()
running = True

# Boucle principale
while running:
    dt = clock.tick(60) / 1000

    # Défilement vertical
    scroll += 100 * dt 
    if scroll >= bg_height:
        scroll = 0

    # Fond infini
    for i in range(tiles):
        screen.blit(bg, (0, -i * bg_height + scroll))

    for event in pg.event.get():
        if event.type == QUIT:
            running = False

    # Déplacement du vaisseau
    keys = pg.key.get_pressed()
    if keys[K_LEFT] and x > 0:
        x -= speed * dt
        direction = False
    if keys[K_RIGHT] and x < SCREEN_WIDTH - 96:
        x += speed * dt
        direction = True

    screen.blit(ship, (x, 480))
    screen.blit(laser, (0, 0))

    pg.display.update()

pg.quit()
