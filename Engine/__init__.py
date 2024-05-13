import pygame as pg

from Engine.config import Screen, Game

TILE_SIZE: int = config.TILE_SIZE
LOGS_FORMAT: str = ".log"
SAVES_FORMAT: str = ".json"
WORLD_SAVES: str = "data/levels/"

def draw_level(sky_level: list, grass_level: list, sun: list, lowest_level: list):
    if TILE_SIZE == -100:
        return "Haven't set tile sizes!"
    else:
        for y, row in enumerate(lowest_level):
            for x, tile_type in enumerate(row):
                if tile_type == 'stone':  # Если тип тайла - вода, рисуем синий прямоугольник
                    pg.draw.rect(Screen.screen, Game.blocks.get('stone'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tile_type == 'andesite':  # Если тип тайла - вода, рисуем синий прямоугольник
                    pg.draw.rect(Screen.screen, Game.blocks.get('andesite'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tile_type == 'diorite':  # Если тип тайла - вода, рисуем синий прямоугольник
                    pg.draw.rect(Screen.screen, Game.blocks.get('diorite'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for y, row in enumerate(grass_level):
            for x, tile_type in enumerate(row):
                if tile_type == 'grass':
                    pg.draw.rect(Screen.screen, Game.blocks.get('grass'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif tile_type == 'darker_grass':
                    pg.draw.rect(Screen.screen, Game.blocks.get('darker_grass'),
                                 (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for y, row in enumerate(sky_level):
            for x, tile_type in enumerate(row):
                if tile_type == 'sky':
                    pg.draw.rect(Screen.screen, Game.blocks.get('sky'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for y, row in enumerate(sun):
            for x, tile_type in enumerate(row):
                if tile_type == 'sun':
                    pg.draw.rect(Screen.screen, Game.blocks.get('sun'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))