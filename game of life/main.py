import copy

import pygame as p
import random
#
WIDTH = 640  # ширина игрового окна
HEIGHT = 640 # высота игрового окна
FPS = 60 # частота кадров в секунду

# создаем игру и окно
p.init() # init запускает pygame.
screen = p.display.set_mode((WIDTH, HEIGHT)) #окно программы, задаем его размеры в настройках.
p.display.set_caption("Жизнь") # заголовок окна
clock = p.time.Clock() # частота выполнения за одну секунду.

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем двумерный массив, и заполняем поле.
current_gen = [[random.randint(0,1) for j in range(WIDTH // 20)] for i in range(HEIGHT // 20)]
# Создаем матрицу для след. поколения
next_gen=[[0 for j in range(WIDTH // 20)] for j in range(HEIGHT // 20)]

#---
def findNeighbors(current_gen,x,y):
    # Ф-ция ищет соседей
    # в пустой клетке, рядом с которой ровно 3 живые клетки, зарождается жизнь
    # если у живой клетки есть 2 или 3 живых соседки, то эта клетка продолжает жить
    # если у живой клетки меньше 2 или больше 3 живых соседки, клетка умирает
    count = 0
    for iY in range(y-1, y+2): # цикл от 0 до 3(не включая 3)
        for jX in range(x-1, x+2): # цикл от 0 до 3(не включая 3)
            print(current_gen[iY][jX], end=', ')
            if current_gen[iY][jX] == 1:
                count +=1
    if current_gen[y][x] == 1: # Если проверяемый элем. == 1
        count -=1
        if count == 2 or count == 3:
            return 1
        else:
            return 0
    else:
        if count == 3:
            print('Новая жизнь: ', 1)
            return 1
        else:
            return 0

    # if current_gen[y][x]: # Если проверяемый элем. == 1
    #     return count == 3 or count == 4
    # else:
    #     return count == 3


#---
# def run(current_gen):
#     while True:  # Бесконечный цикл
#         clock.tick(FPS)  # частота выполнения цикла за одну секунду.
#         # выполнять цикл while {FPS} раз в секунду
#         for event in p.event.get():  # смотрим события
#             if event.type == p.QUIT:  # p.QUIT код: 256
#                 exit(0)
#             else:
#                 # grid(current_gen) # сетка
#                 # Рендеринг отрисовка
#                 screen.fill(WHITE)
#                 # Рисуем сетку под размер окна
#                 for i in range(0, HEIGHT // 20):
#                     p.draw.line(screen, BLACK, (0, i * 20), (WIDTH, i * 20))
#                     #
#                 for j in range(0, WIDTH // 20):
#                     p.draw.line(screen, BLACK, (j * 20, 0), (j * 20, HEIGHT))
#                 # ----------------------------------------------------------------------------
#                 # Идем по массиву (матрице) current_gen
#                 for x in range(1, (WIDTH // 20) - 1):
#                     for y in range(1, (HEIGHT // 20) - 1):
#                         # Рисуем только живые клетки
#                         if current_gen[y][x] == 1:
#                             #pass
#                             p.draw.rect(screen, (GREEN), (x * 20, y * 20, 20, 20))
#                         else: # иначе проверяем соседей, добавляем клетки в массив "след.поколения"
#                             next_gen[y][x] = findNeighbors(current_gen, x, y)
#
#                 # Полностью копируем заполненный массив "след. поколения" в current_gen "текущее поколение
#                 current_gen = copy.deepcopy(next_gen)
#                 # после отрисовки всего, обновляем экран (Показываем)
#                 p.display.update()
# #---

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #run(current_gen)
    while True:  # Бесконечный цикл
        clock.tick(FPS)  # частота выполнения цикла за одну секунду.
        # выполнять цикл while {FPS} раз в секунду
        for event in p.event.get():  # смотрим события
            if event.type == p.QUIT:  # p.QUIT код: 256
                exit(0)
            else:
                # grid(current_gen) # сетка
                # Рендеринг отрисовка
                screen.fill(WHITE)
                # Рисуем сетку под размер окна
                for i in range(0, HEIGHT // 20):
                    p.draw.line(screen, BLACK, (0, i * 20), (WIDTH, i * 20))
                    #
                for j in range(0, WIDTH // 20):
                    p.draw.line(screen, BLACK, (j * 20, 0), (j * 20, HEIGHT))
                # ----------------------------------------------------------------------------

                for x in range(1, (WIDTH // 20) - 1):
                    for y in range(1, (HEIGHT // 20) - 1):
                        # Рисуем только живые клетки
                        if current_gen[y][x] == 1:
                            p.draw.rect(screen, (GREEN), (x * 20, y * 20, 20, 20))
                        next_gen[y][x] = findNeighbors(current_gen, x, y)

                current_gen = copy.deepcopy(next_gen)
                # после отрисовки всего, обновляем экран (Показываем)
                p.display.update()
    #
    #
    # #print(f'fps: {clock.get_fps()}')
    # #print(screen.get_width() // 20, screen.get_height() // 20)
