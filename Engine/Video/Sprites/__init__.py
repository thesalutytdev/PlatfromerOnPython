import pygame as pg

class Sprites(pg.sprite.Sprite):
    def create(self, color: tuple, x: int, y: int):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)