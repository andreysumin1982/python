import pygame as p
import random
#
WIDTH = 640  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
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
#
def grid():
    # Рендеринг отрисовка
    screen.fill(WHITE)
    # Рисуем сетку под размер окна
    for i in range(0, screen.get_height()//20):
        p.draw.line(screen, BLACK, (0, i*20), (screen.get_width(), i*20))
    for j in range(0, screen.get_width()//20):
        p.draw.line(screen, BLACK, (j*20, 0), (j*20, screen.get_height()))
    # Создаем двумерный массив, и заполняем поле.
    massiv = [[random.choice([0 , 1]) for j in range(screen.get_width()//20)] for i in range(screen.get_height()//20)]
    print(massiv)
    for i in range(0, len(massiv)):
        for j in range(0, len(massiv[i])):
            p.draw.rect(screen, (155*massiv[i][j]%156, 128, 0), [i*20, j*20, 20, 20])
        #print()

    # после отрисовки всего, обновляем экран (Показываем)
    p.display.update()

#
def run():
    while True: # Бесконечный цикл
        clock.tick(FPS) # частота выполнения цикла за одну секунду.
                        # выполнять цикл while {FPS} раз в секунду
        for event in p.event.get(): # смотрим события
            if event.type == p.QUIT: # p.QUIT код: 256
               return
            else:
                grid() # сетка

#


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run() #
    print(f'fps: {clock.get_fps()}')
    print(screen.get_width() // 20, screen.get_height() // 20)
    #
