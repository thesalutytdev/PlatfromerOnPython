import Engine.JSON
import Engine.Events
import Engine.Video
import Engine.gamecrasher
import Engine.tick as Tick
import World
from Player import Player

from os import environ
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
while Game.is_running:
    Clock.tick(Game.FPS)
    Tick.Tick.tick(Tick.Tick)
    Player.__init__(Player, "TheSALUTYT", "assets/player/saves/save.json")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Game.is_running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                Game.is_running = False
            elif event.key == pg.K_t:
                Events.key_event(Events, "t")
            elif event.key == pg.K_g:
                have_generated_world = True
                Events.on_world_gen(Events)
                Engine.draw_level(sky_level, grass_level, sun, lowest_level)
                Events.on_world_generated(Events)
            elif event.key == pg.K_r:
                have_generated_world = True
                Events.on_world_regen(Events)
                Engine.draw_level(
                    World.generate_sky(),
                      World.grass_level(),
                        World.create_sun(),
                          World.generate_lowest())
            elif event.key == pg.K_w:
                Events.key_event(Events, "w")
            elif event.key == pg.K_a:
                Events.key_event(Events, "a")
            elif event.key == pg.K_s:
                Events.key_event(Events, "s")
            elif event.key == pg.K_d:
                Events.key_event(Events, "d")
            elif event.key == pg.K_e:
                Events.key_event(Events, "e")
            elif event.key == pg.K_f:
                Events.key_event(Events, "f")
            elif event.key == pg.K_z:
                Events.key_event(Events, "z")
            elif event.key == pg.K_x:
                Events.key_event(Events, "x")
            elif event.key == pg.K_c:
                Events.key_event(Events, "c")
            elif event.key == pg.K_v:
                Events.key_event(Events, "v")
            elif event.key == pg.K_b:
                Events.key_event(Events, "b")
            elif event.key == pg.K_n:
                Events.key_event(Events, "n")
            elif event.key == pg.K_m:
                Events.key_event(Events, "m")
            elif event.key == pg.K_1:
                Events.key_event(Events, "1")
            elif event.key == pg.K_2:
                Events.key_event(Events, "2")
            elif event.key == pg.K_3:
                Events.key_event(Events, "3")
            elif event.key == pg.K_4:
                Events.key_event(Events, "4")
            elif event.key == pg.K_5:
                Events.key_event(Events, "5")
            elif event.key == pg.K_6:
                Events.key_event(Events, "6")
            elif event.key == pg.K_7:
                Events.key_event(Events, "7")
            elif event.key == pg.K_8:
                Events.key_event(Events, "8")
            elif event.key == pg.K_9:
                Events.key_event(Events, "9")
            elif event.key == pg.K_0:
                Events.key_event(Events, "0")
            elif event.key == pg.K_SPACE:
                Events.key_event(Events, "SPACE")
            elif event.key == pg.K_LSHIFT:
                Events.key_event(Events, "LSHIFT")
            elif event.key == pg.K_LCTRL:
                Events.key_event(Events, "LCTRL")
        Player.game_saver(Player)
    pg.display.update()
Engine.gamecrasher.crash("Exited")