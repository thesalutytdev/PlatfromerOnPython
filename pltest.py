import Engine.JSON
import Engine.Events
import Engine.Video
import World
from Player import Player

from os import environ
import os
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '0'
import pygame as pg

pg.init()
Screen = Engine.config.Screen
Game = Engine.config.Game
Events = Engine.Events.Events
Json = Engine.JSON.JSON
Clock = pg.time.Clock()
Screen.__init__(Screen)
pg.display.set_caption(Screen.title)
pg.display.set_icon(Screen.icon)
lowest_level = World.generate_lowest()
sky_level = World.generate_sky()
grass_level = World.grass_level()
sun = World.create_sun()
have_generated_world = False
TILE_SIZE = 10
Events.on_load(Events)

# Load player image
player_image = pg.image.load("assets/pack/default/window/images/player.png")
player_rect = player_image.get_rect()
player_rect.topleft = (100, 100)  # Initial position of the player

# Gravity settings
gravity = 0.5
player_velocity_y = 0
is_on_ground = False

def check_collision(rect, blocks):
    for block in blocks:
        if rect.colliderect(block):
            return block
    return None

def get_blocks():
    # This function should return a list of rects representing the blocks in the world
    blocks = []
    for block_list in [grass_level, lowest_level, sky_level]:
        for block in block_list:
            blocks.append(pg.Rect(block.x, block.y, TILE_SIZE, TILE_SIZE))
    return blocks

# Initialize player once
Player.__init__(Player, "TheSALUTYT", "assets/player/saves/save.json")

while Game.is_running:
    Clock.tick(Game.FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Game.is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                Game.is_running = False
            elif event.key == pg.K_g:
                have_generated_world = True
                Events.on_world_gen(Events)
                Engine.draw_level(sky_level, grass_level, sun, lowest_level)
                Events.on_world_generated(Events)
            elif event.key == pg.K_r:
                have_generated_world = True
                Events.on_world_regen(Events)
                Engine.draw_level(World.generate_sky(), World.grass_level(), World.create_sun(), World.generate_lowest())
        Player.game_saver(Player)

    # Apply gravity
    if not is_on_ground:
        player_velocity_y += gravity
    player_rect.y += player_velocity_y

    # Check for collisions with blocks
    blocks = get_blocks()
    collision_block = check_collision(player_rect, blocks)
    if collision_block:
        player_rect.bottom = collision_block.top
        player_velocity_y = 0
        is_on_ground = True
    else:
        is_on_ground = False

    # Draw the player image
    Screen.surface.blit(player_image, player_rect)

    pg.display.update()
exit("[Main] Game exited")