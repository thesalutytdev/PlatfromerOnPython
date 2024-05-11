import pygame as pg
import json

import Player
import World

pg.init()

try:
    ru_lang_raw = ""
    en_lang_raw = ""
    with open("./assets/lang/ru.json", "r") as f:
        ru_lang_raw = f.read()
    with open("./assets/lang/en.json", "r") as f:
        en_lang_raw = f.read()
    ru_lang = json.loads(ru_lang_raw.encode("utf-8"))
    en_lang = json.loads(en_lang_raw.encode("utf-8"))
except FileNotFoundError as ex:
    exit(ex)

class Screen:
    screen = None
    width = 600
    height = 300
    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255)
    }
    game_settings_raw = ""
    with open("./assets/player/settings/settings.json", "r") as f:
        game_settings_raw = f.read()
    game_settings = json.loads(game_settings_raw)
    lang = game_settings["lang"]
    title = ""
    icon = pg.image.load(game_settings["icon"])
    font = pg.font.Font(game_settings["font"], 40)
    if lang == "ru":
        title = ru_lang["platformer.window.title"]
    elif lang == "en":
        title = en_lang["platformer.window.title"]

    def __init__(self):
        self.screen = pg.display.set_mode((self.width, self.height))

    def set_width(self, width: int):
        self.width = width
        self.screen = pg.display.set_mode((self.width, self.height))

class Game:
    is_running = True
    player = pg.image.load("./assets/window/images/player.png")
    blocks = {
        "stone": (87, 84, 78),
        "grass": (0, 255, 0),
        "sky": (122, 192, 230),
        "water": (0, 0, 255),
        "andesite": (122, 118, 108),
        "diorite": (163, 163, 163),
        "sun": (225, 240, 22)
    }

Screen.__init__(Screen)
pg.display.set_caption(Screen.title)
pg.display.set_icon(Screen.icon)
lowest_level = World.generate_lowest()
sky_level = World.generate_sky()
grass_level = World.grass_level()
sun = World.create_sun()
TILE_SIZE = 10

while Game.is_running:
    pg.display.update()
    # Player.Player.game_saver(Player)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Game.is_running = False
            pg.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                Screen.screen.fill(Screen.colors.get("red"))
            elif event.key == pg.K_a:
                Screen.screen.fill(Screen.colors.get("green"))
            elif event.key == pg.K_s:
                Screen.screen.fill(Screen.colors.get("blue"))
                Screen.font.render(self=pg.font,
                                   text=Screen.title,
                                   antialias=False,
                                   color=Screen.colors.get("white"))

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
    for y, row in enumerate(sky_level):
        for x, tile_type in enumerate(row):
            if tile_type == 'sky':
                pg.draw.rect(Screen.screen, Game.blocks.get('sky'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    for y, row in enumerate(sun):
        for x, tile_type in enumerate(row):
            if tile_type == 'sun':
                pg.draw.rect(Screen.screen, Game.blocks.get('sun'), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

pg.quit()