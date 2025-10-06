import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Main Menu")

MenuButton = pg.image.load('Assets/buttons/MENU.png')
PauseButton = pg.image.load('Assets/buttons/PAUSE.png')
PlayButton = pg.image.load('Assets/buttons/PLAY.png')
QuitButton = pg.image.load('Assets/buttons/QUIT.png')
CrossButton = pg.image.load('Assets/buttons/x.png')

game_paused = False

font = pg.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
while run:

    screen.fill((52, 78, 91))

    if game_paused == True:
        pass
    else:
        draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_paused = True
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()