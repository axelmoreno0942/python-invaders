import pygame as pg
import random
import sys
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

# Images
Menu = pg.transform.scale(pg.image.load('Assets/menu.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
Fond = pg.transform.scale(pg.image.load('Assets/background.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
Logo = pg.transform.scale(pg.image.load('Assets/logo.png'), (302, 305.6))
MenuButton = pg.transform.scale(pg.image.load('Assets/buttons/MENU.png'), (192, 55))
PlayButton = pg.transform.scale(pg.image.load('Assets/buttons/PLAY.png'), (116, 37))
QuitButton = pg.transform.scale(pg.image.load('Assets/buttons/QUIT.png'), (109, 47))

# Rect
menu_button = MenuButton.get_rect(center=(SCREEN_WIDTH // 2, 400))
play_rect = PlayButton.get_rect(center=(SCREEN_WIDTH // 2, 480))
quit_rect = QuitButton.get_rect(center=(SCREEN_WIDTH // 2, 540))

# Mode set
menu_active = True
game_active = False

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

def show_menu():
    screen.blit(Menu, (0, 0))
    screen.blit(Logo, (89, 25))
    screen.blit(MenuButton, menu_button)
    screen.blit(PlayButton, play_rect)
    screen.blit(QuitButton, quit_rect)
    pg.display.flip()

# Clock
clock = pg.time.Clock()
running = True

# Game
while running:
    dt = clock.tick(60) / 1000

    # --- Gestion des événements ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

        if menu_active:
            pg.mixer.music.pause()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    menu_active = False
                    game_active = True
                elif quit_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()

        elif game_active:
            pg.mixer.music.unpause()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                game_active = False
                menu_active = True

    # --- Logique du jeu et rendu ---
    if menu_active:
        show_menu()

    elif game_active:
        # Scrolling du fond
        scroll += 100 * dt 
        if scroll >= bg_height:
            scroll = 0

        for i in range(tiles):
            screen.blit(bg, (0, -i * bg_height + scroll))

        # Déplacement du vaisseau
        keys = pg.key.get_pressed()
        if keys[K_LEFT] and shipX > 0:
            shipX -= speed * dt
        if keys[K_RIGHT] and shipX < SCREEN_WIDTH - 96:
            shipX += speed * dt

        # Affichage du vaisseau
        screen.blit(ship, (shipX, shipY))
        show_score(scoreX, scoreY)

    pg.display.update()

pg.quit()