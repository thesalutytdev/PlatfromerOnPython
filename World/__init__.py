import json
import random

import Engine
import Engine.config as CFG

WIDTH = CFG.WIDTH
HEIGHT = CFG.HEIGHT

GRASS_LVL = HEIGHT / 3 * 2 + ((HEIGHT / 10) *  1.5)
SUN = HEIGHT / 10 * 2
SKY = HEIGHT / 3 * 2
CLOUDS = SKY / 2

class Layer:
    name: str
    layer_level: int
    blocks: dict
    width: int
    height: int
    def new(self, layer: dict):
        self.name = layer.get('name')
        self.layer_level = layer.get('layer_level')
        self.blocks = layer.get('blocks')
        self.width = layer.get('width')
        self.height = layer.get('height')


def generate_level():
    level = [generate_sky(), grass_level(), create_sun(), generate_lowest()]
    return level
def gen_and_draw():
    Engine.draw_level(generate_sky(), grass_level(), create_sun(), generate_lowest())
def generate_lowest():
    global tile_type
    TILE_SIZE = 10
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = HEIGHT // TILE_SIZE
    world_data = []
    for y in range(TILES_HIGH):
        row = []
        for x in range(int(TILES_WIDE)):
            random_block = random.randint(0, 2)
            if random_block == 0:
                tile_type = 'stone'
            elif random_block == 1:
                tile_type = 'andesite'
            elif random_block == 2:
                tile_type = 'diorite'
            row.append(tile_type)
        world_data.append(row)
    with open(f"{Engine.WORLD_SAVES}lowest.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data

def generate_sky():
    global tile_type
    TILE_SIZE = 10
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = SKY // TILE_SIZE
    world_data = []
    for y in range(int(TILES_HIGH)):
        row = []
        for x in range(int(TILES_WIDE)):
            random_block = random.randint(0, 1)
            if random_block == 0:
                tile_type = 'sky'
            else:
                tile_type = 'sky'
            row.append(tile_type)
        world_data.append(row)
    with open(f"{Engine.WORLD_SAVES}sky.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data
def grass_level():
    global tile_type
    TILE_SIZE = 10
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = GRASS_LVL // TILE_SIZE
    world_data = []
    for y in range(int(TILES_HIGH)):
        row = []
        for x in range(int(TILES_WIDE)):
            random_block = random.randint(0, 1)
            if random_block == 0:
                tile_type = 'grass'
            elif random_block == 1:
                tile_type = 'darker_grass'
            row.append(tile_type)
        world_data.append(row)
    with open(f"{Engine.WORLD_SAVES}grass.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data
def create_sun():
    global tile_type
    WIDTH = SUN
    HEIGHT = SUN
    TILE_SIZE = 10
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = HEIGHT // TILE_SIZE
    sun_data = []
    for y in range(int(TILES_WIDE)):
        row = []
        for x in range(int(TILES_HIGH)):
            row.append('sun')
        sun_data.append(row)
    with open(f"{Engine.WORLD_SAVES}sun.json", "w") as outfile:
        json.dump(sun_data, outfile)
    return sun_data
def create_clouds():
    global tile_type
    WIDTH = CLOUDS
    HEIGHT = CLOUDS
    TILE_SIZE = 30
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HIGH = HEIGHT // TILE_SIZE
    sun_data = []
    for y in range(int(TILES_WIDE)):
        row = []
        for x in range(int(TILES_HIGH)):
            row.append('clouds')
        sun_data.append(row)
    with open(f"{Engine.WORLD_SAVES}clouds.json", "w") as outfile:
        json.dump(sun_data, outfile)
    return sun_data
def generate_custom_layer(custom_layer: dict):
    global tile_type
    WIDTH = custom_layer.get("width")
    HEIGHT = custom_layer.get("height")
    TILE_SIZE = Engine.TILE_SIZE
    TILES_WIDE = WIDTH // TILE_SIZE
    TILES_HEIGHT = HEIGHT // TILE_SIZE
    level_data = []
    for y in range(int(TILES_WIDE)):
        row = []
        for x in range(int(TILES_HEIGHT)):
            blocks_amount = len(custom_layer.get("blocks"))
            blocks = custom_layer.get("blocks")
            random_block = random.randint(0, blocks_amount - 1)
            row.append(blocks[random_block])
        level_data.append(row)
    with open(f"{custom_layer.get('save_to')}{custom_layer.get('name')}.json", "w") as outfile:
        json.dump(level_data, outfile)
    return level_data