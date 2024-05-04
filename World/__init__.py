import json
import random
import Player

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
            random_block = random.randint(0, 3)
            if random_block == 0:  # Случайное определение типа тайла
                tile_type = 'grass'  # Если случайное число равно 0, тип тайла - трава
            elif random_block == 1:
                tile_type = 'stone'  # Если случайное число не равно 0, тип тайла - вода
            elif random_block == 2:
                tile_type = 'andesite'
            elif random_block == 3:
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
            random_block = random.randint(0, 3)
            if random_block == 0:  # Случайное определение типа тайла
                tile_type = 'sky'  # Если случайное число равно 0, тип тайла - трава
            row.append(tile_type)  # Добавление типа тайла в текущую строку
        world_data.append(row)  # Добавление строки в общий список данных о мире
    with open("./lowest.json", "w") as outfile:
        json.dump(world_data, outfile)
    return world_data