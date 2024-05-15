import Engine.JSON
import Engine.Events
import Engine.Video
import World
from Player import Player

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame as pg

pg.init()
Screen = Engine.config.Screen
Game = Engine.config.Game
Events = Engine.Events.Events
Json = Engine.JSON.JSON
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
while Game.is_running:
    Player.__init__(Player, "TheSALUTYT", "assets/player/saves/save.json")

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
                # Engine.Video.draw_layer(sun)
        Player.game_saver(Player)
    pg.display.update()
exit("[Main] Game exited")