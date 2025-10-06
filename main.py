import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((480, 640))
screen = pg.display.set_caption('Python Invaders')
playing = True

while playing:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            playing = False

pg.quit()