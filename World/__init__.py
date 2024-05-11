import json
import random
import Player

world_blocks = {

}
"""
example: 
{
layer:{pos: block_type}
}
"""


def generate_level(player: Player.Player):
    pass
def generate_lowest():
    # Определение параметров мира
    global tile_type
    WIDTH = 600  # Ширина экрана
    HEIGHT = 300 # Высота экрана
    TILE_SIZE = 10  # Размер тайла
    TILES_WIDE = WIDTH // TILE_SIZE  # Количество тайлов по горизонтали
    TILES_HIGH = HEIGHT // TILE_SIZE  # Количество тайлов по вертикали
    # Генерация случайного мира
    world_data = []  # Создание пустого списка для хранения данных о мире
    for y in range(TILES_HIGH):
        row = []  # Создание пустого списка для хранения данных о строке мира
        for x in range(TILES_WIDE):
            random_block = random.randint(0, 2)
            if random_block == 0:
                tile_type = 'stone'  # Если случайное число не равно 0, тип тайла - вода
            elif random_block == 1:
                tile_type = 'andesite'
            elif random_block == 2:
                tile_type = 'diorite'
            row.append(tile_type)  # Добавление типа тайла в текущую строку
        world_data.append(row)  # Добавление строки в общий список данных о мире
    with open("./lowest.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data

def generate_sky():
    # Определение параметров мира
    global tile_type
    WIDTH = 600  # Ширина экрана
    HEIGHT = 200 # Высота экрана
    TILE_SIZE = 10  # Размер тайла
    TILES_WIDE = WIDTH // TILE_SIZE  # Количество тайлов по горизонтали
    TILES_HIGH = HEIGHT // TILE_SIZE  # Количество тайлов по вертикали
    # Генерация случайного мира
    world_data = []  # Создание пустого списка для хранения данных о мире
    for y in range(TILES_HIGH):
        row = []  # Создание пустого списка для хранения данных о строке мира
        for x in range(TILES_WIDE):
            random_block = random.randint(0, 1)
            if random_block == 0:  # Случайное определение типа тайла
                tile_type = 'sky'  # Если случайное число равно 0, тип тайла - трава
            else:
                tile_type = 'sky'
            row.append(tile_type)  # Добавление типа тайла в текущую строку
        world_data.append(row)  # Добавление строки в общий список данных о мире
    with open("./sky.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data
def grass_level():
    global tile_type
    WIDTH = 600 # Ширина экрана
    HEIGHT = 230  # Высота экрана
    TILE_SIZE = 10  # Размер тайла
    TILES_WIDE = WIDTH // TILE_SIZE  # Количество тайлов по горизонтали
    TILES_HIGH = HEIGHT // TILE_SIZE  # Количество тайлов по вертикали
    # Генерация случайного мира
    world_data = []  # Создание пустого списка для хранения данных о мире
    for y in range(TILES_HIGH):
        row = []  # Создание пустого списка для хранения данных о строке мира
        for x in range(TILES_WIDE):
            random_block = random.randint(0, 1)
            if random_block == 0:  # Случайное определение типа тайла
                tile_type = 'grass'  # Если случайное число равно 0, тип тайла - трава
            else:
                tile_type = 'grass'
            row.append(tile_type)  # Добавление типа тайла в текущую строку
        world_data.append(row)  # Добавление строки в общий список данных о мире
    with open("./grass_level.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data
def create_sun():
    global tile_type
    WIDTH = 60  # Ширина экрана
    HEIGHT = 10  # Высота экрана
    TILE_SIZE = 10  # Размер тайла
    TILES_WIDE = WIDTH // TILE_SIZE  # Количество тайлов по горизонтали
    TILES_HIGH = HEIGHT // TILE_SIZE  # Количество тайлов по вертикали
    sun_data = []
    for y in range(TILE_SIZE):
        row = []
        for x in range(TILES_WIDE):
            row.append('sun')
        sun_data.append(row)
    with open("./sun_json.json", "w") as outfile:
        json.dump(sun_data, outfile)
    return sun_data

def gen_sky():
    WIDTH = 300