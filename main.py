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
Pause = pg.transform.scale(pg.image.load('Assets/pause.jpeg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
Fond = pg.transform.scale(pg.image.load('Assets/background.png').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
Logo = pg.transform.scale(pg.image.load('Assets/logo.png'), (302, 305.6))
PauseButton = pg.transform.scale(pg.image.load('Assets/buttons/PAUSE.png'), (214.3, 55))
ResumeButton = pg.transform.scale(pg.image.load('Assets/buttons/RESUME.png'), (183.1, 37))
MenuButton = pg.transform.scale(pg.image.load('Assets/buttons/MENU.png'), (186.3, 55))
PlayButton = pg.transform.scale(pg.image.load('Assets/buttons/PLAY.png'), (116, 37))
QuitButton = pg.transform.scale(pg.image.load('Assets/buttons/QUIT.png'), (109, 47))

# MenuRect
menu_rect = MenuButton.get_rect(center=(SCREEN_WIDTH // 2, 400))
play_rect = PlayButton.get_rect(center=(SCREEN_WIDTH // 2, 480))
quitM_rect = QuitButton.get_rect(center=(SCREEN_WIDTH // 2, 540))

# PauseRect
pause_rect = PauseButton.get_rect(center=(SCREEN_WIDTH // 2, 150))
resume_rect = ResumeButton.get_rect(center=(SCREEN_WIDTH // 2, 370))
quitP_rect = QuitButton.get_rect(center=(SCREEN_WIDTH // 2, 440))

# Game state
game_state = 'menu'
paused_pressed = False

# Background
bg = pg.image.load('Assets/background.png').convert_alpha()
bg = pg.transform.scale(bg, screen.get_size())
bg_height = bg.get_height()
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT / bg_height) + 1

# Player
ship = pg.image.load('Assets/sunny.png').convert_alpha()
ship = pg.transform.scale(ship, (94.8, 122))
shipX = 190
shipY = 480
shipXchange = 0
speed = 250
direction = True

# Enemies
invaderImage = [
    pg.transform.scale(pg.image.load('Assets/adv1.png'), (70.4, 122)),
    pg.transform.scale(pg.image.load('Assets/adv2.png'), (64.6, 122)),
    pg.transform.scale(pg.image.load('Assets/adv3.png'), (95.8, 122))
]

#Invaders code
invaderX = []
invaderY = []
invaderXchange = []
invaderYchange = []
numInvaders = 8

for num in range(numInvaders):
    invaderImage.append(random.choice(invaderImage))
    invaderX.append(random.randint(38, 786))
    invaderY.append(random.randint(18, 192))
    invaderXchange.append(1.2)
    invaderYchange.append(50)
    
# Bullet
bulletImage = pg.transform.scale((pg.image.load('Assets/cannon_ball.png')), (15,15))
bulletX = 0
bulletY = 500
bulletXchange = 0
bulletYchange = 3
bulletstate = "rest"

#collision shot

def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False

def player(x, y):
    screen.blit(ship, (x - 16, y + 10))

def invader(x, y, i):
    screen.blit(invaderImage[i], (x, y))

def bullet(x, y):
    global bulletstate
    screen.blit(bulletImage, (x, y))
    bulletstate = "fire"

# Score
score_val = 0
scoreX = 5
scoreY = 5

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (0,0,0))
    screen.blit(score, (x , y ))

def show_pause_score():
    title_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 48)
    score_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 36)
    title = title_font.render("SCORE", True, (255, 255, 0))  # blanc
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
    score_text = score_font.render(str(score_val), True, (255, 215, 0))  # or
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(title, title_rect)
    screen.blit(score_text, score_rect)


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
    screen.blit(MenuButton, menu_rect)
    screen.blit(PlayButton, play_rect)
    screen.blit(QuitButton, quitM_rect)
    pg.display.flip()

def show_pause():
    screen.blit(Pause, (0, 0))
    screen.blit(PauseButton, pause_rect)
    screen.blit(ResumeButton, resume_rect)
    screen.blit(QuitButton, quitP_rect)
    show_pause_score()
    pg.display.flip()

# Clock
clock = pg.time.Clock()
running = True

# Game
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()

        if game_state == 'menu':
            pg.mixer.music.pause()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    game_state = 'game'
                elif quitM_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()

        elif game_state == 'game':
            pg.mixer.music.unpause()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE and not paused_pressed:
                game_state = 'pause'
                paused_pressed = True
            elif event.type == pg.KEYUP and event.key == pg.K_ESCAPE:
                paused_pressed = False


        elif game_state == 'pause':
            pg.mixer.music.pause()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if resume_rect.collidepoint(mouse_pos):
                    paused_pressed = False
                    game_state = 'game'
                elif quitP_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()



    # --- Logique du jeu et rendu ---
    if game_state == 'menu':
        show_menu()
    
    elif game_state == 'pause':
        show_pause()

    elif game_state == 'game':
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

        #bullet movement
        if keys[K_SPACE]:
            if bulletstate is "rest":
                bullet_X = shipX
                bullet(bullet_X, bulletY)
                bullet_sound = mixer.Sound('bruit du canon.wav')
                bullet_sound.play()

        if bulletY <= 0:
            bulletY = 600
            bulletstate = "rest"
        if bulletstate is "fire":
            bullet(bulletX, bulletY)
            bulletY -= bulletYchange

        #movement of the invader
        for i in range(numInvaders):
        
            if invaderY[i] >= 450:
                if abs(shipX-invaderX[i]) < 80:
                    for j in range(numInvaders):
                        invaderY[j] = 2000
                        explosion_sound = mixer.Sound('Big Explosion Effect Video Mp4 HD Sound.wav')
                        explosion_sound.play()
                game_over()
                break

        if invaderX[i] >= 735 or invaderX[i] <= 0:
            invaderXchange[i] *= -1
            invaderY[i] += invaderYchange[i]

        #Collision 4real
        collision = isCollision(bulletX, invaderX[i],
                                bulletY, invaderY[i])
        if collision:
            score_val += 1
            bulletY = 600
            bulletstate = "rest"
            invaderX[i] = random.randint(64, 736)
            invaderY[i] = random.randint(30, 200)
            invaderXchange[i] *= -1

        invader(invaderX[i], invaderY[i], i)
        
        # Affichage du vaisseau
        screen.blit(ship, (shipX, shipY))
        show_score(scoreX, scoreY)

    pg.display.update()

pg.quit()