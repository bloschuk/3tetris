import pygame
import random

pygame.init()

# установка окна
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30

# гравитация
GRAVITY_SPEED = 0.01
DOWN_SPEED = 5

# размер фигуры
shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)]
]

# класс фигуры
class Tetromino:
    def __init__(self):
        self.shape = random.choice(shapes)
        self.color = (255,0,0)
        self.x = 3
        self.y = 0
        self.fall_counter = 0

    def rotate(self):
        self.shape = [(-y, x) for x, y in self.shape]

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

# создание
tetromino = Tetromino()

# запуск игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetromino.move_left()
            elif event.key == pygame.K_RIGHT:
                tetromino.move_right()
            elif event.key == pygame.K_UP:
                tetromino.rotate()
            elif event.key == pygame.K_DOWN:
                tetromino.move_down()

    # гравитация
    tetromino.fall_counter += GRAVITY_SPEED
    if tetromino.fall_counter >= 1:
        tetromino.y += 1
        tetromino.fall_counter = 0

    # очистка окна
    window.fill(BLACK)

    # отрисовка поля
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, GRAY, rect, 1)

    # отрисовка фигуры
    for x, y in tetromino.shape:
        rect = pygame.Rect((tetromino.x + x) * CELL_SIZE, (tetromino.y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(window, tetromino.color, rect)
        pygame.draw.rect(window, BLACK, rect, 1)

    # обновление экрана
    pygame.display.flip()

pygame.quit()
