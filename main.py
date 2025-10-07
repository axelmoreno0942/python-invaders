import pygame as pg
import random
from pygame.locals import *
import math
from pygame import mixer

pg.init()

# Window
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("McInvaders")
font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 22)

# Background
bg = pg.image.load('Assets/background.png').convert_alpha()
bg = pg.transform.scale(bg, screen.get_size())
bg_height = bg.get_height()
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT / bg_height) + 1

# Player
ship = pg.image.load('Assets/sunny.png').convert_alpha()
ship = pg.transform.scale(ship, (96, 122))
shipX = 190
shipY = 480
speed = 250
direction = True
shipXchange = 0

# Invaders

laser = pg.image.load('Assets/cannon_ball.png').convert_alpha()

# Score
score_val = 0
scoreX = 5
scoreY = 5

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (0,0,0))
    screen.blit(score, (x , y ))

# Game Over
GO = pg.image.load('Assets/buttons/GAME OVER.png')
GO = pg.transform.scale(GO, (322, 48)) #5163 x 755

def game_over():
    screen.blit(GO, ((SCREEN_WIDTH//2)-131, (SCREEN_HEIGHT//2)-24))

# Background Sound
mixer.music.load('Opening.wav')
mixer.music.play(-1)

# Clock
clock = pg.time.Clock()
running = True

# Game
while running:
    dt = clock.tick(60) / 1000

    # Infinite scroll
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
    if keys[K_LEFT] and shipX > 0:
        shipX -= speed * dt
        direction = False
    if keys[K_RIGHT] and shipX < SCREEN_WIDTH - 96:
        shipX += speed * dt
        direction = True

    screen.blit(ship, (shipX, 480))
    #screen.blit(laser, (0, 0))
    show_score(scoreX, scoreY)

    pg.display.update()

pg.quit()