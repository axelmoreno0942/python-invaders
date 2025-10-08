import pygame as pg
import random
import sys
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
Logo = pg.transform.scale(pg.image.load('Assets/logo.png'), (302, 302))
Explosion = pg.transform.scale(pg.image.load('Assets/explosion.png'), (107.8, 100))
Win = pg.transform.scale(pg.image.load('Assets/win.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
WinButton = pg.transform.scale(pg.image.load('Assets/buttons/WIN.png'), (129, 55))
GameOver = pg.transform.scale(pg.image.load('Assets/gameover.jpg').convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
GameOverButton = pg.transform.scale(pg.image.load('Assets/buttons/GAME OVER.png'), (436, 65))
RetryButton = pg.transform.scale(pg.image.load('Assets/buttons/RETRY.png'), (143.6, 37))
PauseButton = pg.transform.scale(pg.image.load('Assets/buttons/PAUSE.png'), (214, 55))
ResumeButton = pg.transform.scale(pg.image.load('Assets/buttons/RESUME.png'), (183, 37))
MenuButton = pg.transform.scale(pg.image.load('Assets/buttons/MENU.png'), (186, 55))
MenubButton = pg.transform.scale(pg.image.load('Assets/buttons/MENUb.png'), (125.1, 37))
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

# WinRect
win_rect = WinButton.get_rect(center=(SCREEN_WIDTH // 2, 50))
menub_rect = MenubButton.get_rect(center=(SCREEN_WIDTH // 2, 270))
quitW_rect = QuitButton.get_rect(center=(SCREEN_WIDTH // 2, 340))

# Game Over Rect
gameover_rect = WinButton.get_rect(center=(85, 50))
retry_rect = RetryButton.get_rect(center=(SCREEN_WIDTH // 2, 300))
menub_rect = MenubButton.get_rect(center=(SCREEN_WIDTH // 2, 370))
quitW_rect = QuitButton.get_rect(center=(SCREEN_WIDTH // 2, 440))

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
ship = pg.transform.scale(ship, (95, 122))
shipX = (SCREEN_WIDTH - ship.get_width()) // 2
shipY = 480
speed = 250

# Invader images
invaderImgs = [
    pg.transform.scale(pg.image.load('Assets/adv1.png'), (70, 122)),
    pg.transform.scale(pg.image.load('Assets/adv2.png'), (65, 122)),
    pg.transform.scale(pg.image.load('Assets/adv3.png'), (96, 122))
]

# Invaders state
invaderX = []
invaderY = []
invaderXchange = []
invaderYchange = []
invader_img_index = []
numInvaders = 8
invader_speed = 80 

for _ in range(numInvaders):
    img_idx = random.randrange(len(invaderImgs))
    invader_img_index.append(img_idx)
    img_w = invaderImgs[img_idx].get_width()
    x = random.randint(0, SCREEN_WIDTH - img_w)
    y = random.randint(0, 180)
    invaderX.append(x)
    invaderY.append(y)
    invaderXchange.append(1)
    invaderYchange.append(40)

# Bullet
bulletImage = pg.transform.scale(pg.image.load('Assets/cannon_ball.png'), (15, 15))
bulletX = 0
bulletY = SCREEN_HEIGHT + 10
bulletYchange = 300
bulletstate = "rest"

# collision shot
def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance <= 30 

explosions = []
EXPLOSION_DURATION = 0.3

def player(x, y):
    screen.blit(ship, (x, y))

def invader(x, y, img):
    screen.blit(invaderImgs[img], (int(x), int(y)))

def fire_bullet(x, y):
    global bulletstate
    screen.blit(bulletImage, (x, y))
    bulletstate = "fire"

# Score
score_val = 0
scoreX = 5
scoreY = 5

def show_score(x, y):
    score = font.render("Score: " + str(score_val), True, (0,0,0))
    screen.blit(score, (x, y))

def show_pause_score():
    title_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 48)
    score_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 36)
    title = title_font.render("SCORE", True, (255, 255, 0))
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
    score_text = score_font.render(str(score_val), True, (255, 215, 0))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
    screen.blit(title, title_rect)
    screen.blit(score_text, score_rect)

def show_win_score():
    title_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 48)
    score_font = pg.font.Font('Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 36)
    title = title_font.render("SCORE", True, (255, 255, 255))
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 180))
    score_text = score_font.render(str(score_val), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))
    screen.blit(title, title_rect)
    screen.blit(score_text, score_rect)

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

def show_win():
    screen.blit(Win, (0, 0))
    screen.blit(WinButton, win_rect)
    screen.blit(MenubButton, menub_rect)
    screen.blit(QuitButton, quitW_rect)
    show_win_score()
    pg.display.flip()

def show_gameover():
    screen.blit(GameOver, (0, 0))
    screen.blit(GameOverButton, gameover_rect)
    screen.blit(RetryButton, retry_rect)
    screen.blit(MenubButton, menub_rect)
    screen.blit(QuitButton, quitW_rect)
    show_win_score()
    pg.display.flip()

# Clock
clock = pg.time.Clock()
running = True

# Game loop
while running:
    dt = clock.tick(60) / 1000.0

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
                    score_val = 0
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

        elif game_state == 'win':
            pg.mixer.music.pause()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if menub_rect.collidepoint(mouse_pos):
                    game_state = 'menu'
                elif quitW_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()
            try:
                win_sound = mixer.Sound('win.wav')
                win_sound.play()
            except Exception: 
                pass

        elif game_state == 'gameover':
            pg.mixer.music.pause()
            gameover_sound = mixer.Sound('Acecri.wav')
            gameover_sound.play()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if retry_rect.collidepoint(mouse_pos):
                    score_val=0
                    game_state = 'game'
                elif menub_rect.collidepoint(mouse_pos):
                    game_state = 'menu'
                elif quitW_rect.collidepoint(mouse_pos):
                    pg.quit()
                    sys.exit()

    if game_state == 'menu':
        show_menu()

    elif game_state == 'pause':
        show_pause()

    elif game_state == 'win':
        show_win()

    elif game_state == 'gameover':
        show_gameover()

    elif game_state == 'game':
        scroll += 100 * dt
        if scroll >= bg_height:
            scroll = 0
        for i in range(tiles):
            screen.blit(bg, (0, -i * bg_height + scroll))

        # Player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and shipX > 0:
            shipX -= speed * dt
        if keys[pg.K_RIGHT] and shipX < SCREEN_WIDTH - ship.get_width():
            shipX += speed * dt

        # Fire bullet
        if keys[pg.K_SPACE]:
            if bulletstate == "rest":
                bulletX = shipX + ship.get_width() // 2 - bulletImage.get_width() // 2
                bulletY = shipY
                fire_bullet(bulletX, bulletY)
                try:
                    bullet_sound = mixer.Sound('bulletfire.wav')
                    bullet_sound.play()
                except Exception:
                    pass

        # Bullet fired
        if bulletstate == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletYchange * dt
            if bulletY <= -bulletImage.get_height():
                bulletY = SCREEN_HEIGHT + 10
                bulletstate = "rest"

        # Update invaders
        for i in range(numInvaders):
            invaderX[i] += invaderXchange[i] * invader_speed * dt
            img_w = invaderImgs[invader_img_index[i]].get_width()
            if invaderX[i] <= 0:
                invaderX[i] = 0
                invaderXchange[i] *= -1
                invaderY[i] += invaderYchange[i]
            elif invaderX[i] + img_w >= SCREEN_WIDTH:
                invaderX[i] = SCREEN_WIDTH - img_w
                invaderXchange[i] *= -1
                invaderY[i] += invaderYchange[i]

            if invaderY[i] + invaderImgs[invader_img_index[i]].get_height() >= shipY:
                game_state = 'gameover'
                try:
                    explosion_sound = mixer.Sound('explosion.wav')
                    explosion_sound.play()
                except Exception:
                    pass
                for j in range(numInvaders):
                    invaderY[j] = 2000
                break

            if bulletstate == "fire":
                bx = bulletX + bulletImage.get_width() / 2
                by = bulletY + bulletImage.get_height() / 2
                ix = invaderX[i] + invaderImgs[invader_img_index[i]].get_width() / 2
                iy = invaderY[i] + invaderImgs[invader_img_index[i]].get_height() / 2

                if isCollision(bx, by, ix, iy):
                    score_val += 1
                    bulletY = SCREEN_HEIGHT + 10
                    bulletstate = "rest"
                    try:
                        hit_sound = mixer.Sound('explosion.wav')
                        hit_sound.play()
                    except Exception:
                        pass

                    explosions.append((invaderX[i], invaderY[i], pg.time.get_ticks() / 1000.0))
                    img_idx = random.randrange(len(invaderImgs))
                    invader_img_index[i] = img_idx
                    invaderX[i] = random.randint(0, SCREEN_WIDTH - invaderImgs[img_idx].get_width())
                    invaderY[i] = random.randint(0, 150)
                    invaderXchange[i] *= -1

            invader(invaderX[i], invaderY[i], invader_img_index[i])
            current_time = pg.time.get_ticks() / 1000.0
            for exp in explosions[:]:
                x, y, start_time = exp
                if current_time - start_time < EXPLOSION_DURATION:
                    screen.blit(Explosion, (x, y))
                else:
                    explosions.remove(exp)

        player(shipX, shipY)
        show_score(scoreX, scoreY)
        
        if score_val >= 30:
            game_state = 'win'

    pg.display.update()

pg.quit()