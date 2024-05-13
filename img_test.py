import pygame as pg

import Utils

pg.init()
myimage = pg.image.load("assets/pack/default/window/images/player_new.png")
imagerect = myimage.get_rect()
screen = pg.display.set_mode((600, 300))
is_running = True
while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    screen.fill((0, 0, 0))
    screen.blit(myimage, imagerect)
    pg.display.flip()
pg.quit()