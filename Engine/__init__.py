import Engine.Video
from Engine.config import Screen, Game

TILE_SIZE: int = config.TILE_SIZE
LOGS_FORMAT: str = ".log"
SAVES_FORMAT: str = ".json"
WORLD_SAVES: str = "data/levels/"
BLOCKS_JSON: str = "game_cash/blocks.json"

def draw_level(sky_level: list, grass_level: list, sun: list, lowest_level: list):
    Engine.Video.draw_layer(lowest_level)
    Engine.Video.draw_layer(grass_level)
    Engine.Video.draw_layer(sky_level)
    Engine.Video.draw_layer(sun)