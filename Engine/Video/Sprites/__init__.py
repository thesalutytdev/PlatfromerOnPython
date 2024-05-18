import pygame as pg


class Sprites(pg.sprite.Sprite):
    class Groups:
        groups: dict

        def create_group(self, group_name: str):
            group = pg.sprite.Group()
            self.groups.update({group_name: group})

    def create(self, color: tuple, x: int, y: int):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
