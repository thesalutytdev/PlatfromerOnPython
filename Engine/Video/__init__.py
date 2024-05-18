import json

import pygame as pg

import Engine.config as CFG

game_blocks = CFG.Game.blocks
Screen = CFG.Screen
TILE_SIZE = CFG.TILE_SIZE
def draw_layer(layer: list):
    for y, row in enumerate(layer):
        for x, tile_type in enumerate(row):
            if tile_type in game_blocks:
                pg.draw.rect(Screen.screen, game_blocks.get(tile_type),
                          (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            else:
                print("[Engine::Video] Invalid block in layer configuration")
                return "Invalid block!"
def draw_image(image_path: str):
    image = pg.image.load(image_path)
    pg.sprite.Sprite.add()