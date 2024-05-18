import json
import assets.pack.current.pack_resources as pack
import pygame as pg
from screeninfo import get_monitors

WIDTH = 1000
HEIGHT = 800

try:
    ru_lang_raw = ""
    en_lang_raw = ""
    with open("assets/pack/default/lang/ru.json", "r") as f:
        ru_lang_raw = f.read()
    with open("assets/pack/default/lang/en.json", "r") as f:
        en_lang_raw = f.read()
    global ru_lang
    ru_lang = json.loads(ru_lang_raw)
    global en_lang
    en_lang = json.loads(en_lang_raw)
except FileNotFoundError as ex:
    exit(ex)

class Screen:
    screen = None
    width = WIDTH
    height = HEIGHT
    colors = pack.COLORS
    game_settings_raw = ""
    with open("./assets/player/settings/settings.json", "r") as f:
        game_settings_raw = f.read()
    game_settings = json.loads(game_settings_raw)
    lang = game_settings["lang"]
    title = ""
    icon = pack.icon # pg.image.load(game_settings["icon"])
    if lang == "ru":
        title = ru_lang["platformer.window.title"]
    elif lang == "en":
        title = en_lang["platformer.window.title"]

    def __init__(self):
        self.screen = pg.display.set_mode((self.width, self.height))
    def set_width(self, width: int):
        self.width = width
        self.screen = pg.display.set_mode((self.width, self.height))
    def get_user_screen_config(self):
        for monitor in get_monitors():
            WIDTH = monitor.width
            HEIGHT = monitor.height
        return [WIDTH, HEIGHT]
    def screen_filler(self, color: tuple):
        self.screen.fill(color)
class Game:
    FPS = 60
    is_running = True
    player = pg.image.load("assets/pack/default/window/images/player.png")
    blocks = pack.BLOCKS
    TILE_SIZE = 10

TILE_SIZE = Game.TILE_SIZE