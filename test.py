# Импорт библиотек
import pygame  # Импорт библиотеки Pygame для создания графического интерфейса
import json  # Импорт библиотеки json для работы с JSON-файлами
import random  # Импорт библиотеки random для генерации случайных чисел

# Определение параметров мира
WIDTH = 800  # Ширина экрана
HEIGHT = 600  # Высота экрана
TILE_SIZE = 10  # Размер тайла
TILES_WIDE = WIDTH // TILE_SIZE  # Количество тайлов по горизонтали
TILES_HIGH = HEIGHT // TILE_SIZE  # Количество тайлов по вертикали

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Генерация случайного мира
world_data = []  # Создание пустого списка для хранения данных о мире
for y in range(TILES_HIGH):
    row = []  # Создание пустого списка для хранения данных о строке мира
    for x in range(TILES_WIDE):
        if random.randint(0, 1) == 0:  # Случайное определение типа тайла
            tile_type = 'grass'  # Если случайное число равно 0, тип тайла - трава
        else:
            tile_type = 'water'  # Если случайное число не равно 0, тип тайла - вода
        row.append(tile_type)  # Добавление типа тайла в текущую строку
    world_data.append(row)  # Добавление строки в общий список данных о мире

# Сохранение сгенерированного мира в файл JSON
with open('world.json', 'w') as outfile:
    json.dump(world_data, outfile)  # Запись данных о мире в файл в формате JSON

# Основной игровой цикл
running = True  # Переменная для контроля работы игрового цикла
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Проверка на закрытие окна
            running = False  # Завершение игрового цикла при закрытии окна

    # Отрисовка мира
    for y, row in enumerate(world_data):
        for x, tile_type in enumerate(row):
            if tile_type == 'grass':  # Если тип тайла - трава, рисуем зеленый прямоугольник
                pygame.draw.rect(screen, (0, 255, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile_type == 'water':  # Если тип тайла - вода, рисуем синий прямоугольник
                pygame.draw.rect(screen, (0, 0, 255), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Обновление экрана
    pygame.display.update()  # Обновление отображения на экране

# Завершение работы Pygame
pygame.quit()  # Выход из Pygame