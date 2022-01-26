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
#
# Создаем двумерный массив, и заполняем поле.
matrix = [[random.randint(0, 1) for j in range(3)] for i in range(3)]
for i in matrix:
# Столбцы
    i.insert(0, 0)
    i.insert(0, 0) # В начале

    i.append(0)
    i.append(0)    # В конце

    # Создаем массив [0,0 ..]
massZero = [0 for i in range(0, len(matrix[0]))]
    # Строки
matrix.insert(0, massZero)
matrix.insert(0, massZero) # В начале

matrix.append(massZero)
matrix.append(massZero) # В конце
#--
# Создаем матрицу для след. поколения
matrixZero = [[0 for j in range(0, len(matrix))] for i in range(0, len(matrix))]

#
def grid(massiv):
    # Рендеринг отрисовка
    screen.fill(WHITE)
    # Рисуем сетку под размер окна
    for i in range(0, screen.get_height()//20):
        p.draw.line(screen, BLACK, (0, i*20), (screen.get_width(), i*20))
        #
    for j in range(0, screen.get_width()//20):
        p.draw.line(screen, BLACK, (j*20, 0), (j*20, screen.get_height()))
    #----------------------------------------------------------------------------
    # Идем по матрице и отображанм на сетке
    #massiv = [[random.choice([0 , 1]) for j in range(32)] for i in range(32)]
    for i in range(0,len(massiv)):
        for j in range(0, len(massiv[i])):
            #print(j, massiv[i][j])
            if massiv[i][j] == 1:
                p.draw.rect(screen, (GREEN), (j*20, i*20, 20, 20))      #1 - Life
            else:
                p.draw.rect(screen, (0,150,240), (j*20, i*20, 20, 20))  #0 - Death
            print(massiv[j], end='\n')
        print(40*'-')
    # после отрисовки всего, обновляем экран (Показываем)
    p.display.update()
#--
def findNeighbors(x, y, matrix):
    # Ф-ция ищет соседей
    count = 0 # это счетчик
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0): #
                pass
            else:
                if (matrix[x + i][y + j] == 1):
                    count+=1
    return count # возвращаем число соседей
#--

#
def run():
    while True: # Бесконечный цикл
        clock.tick(FPS) # частота выполнения цикла за одну секунду.
                        # выполнять цикл while {FPS} раз в секунду
        for event in p.event.get(): # смотрим события
            if event.type == p.QUIT: # p.QUIT код: 256
               return
            else:
                matrix
                grid(matrix) # сетка

#

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run() #
    print(f'fps: {clock.get_fps()}')
    print(screen.get_width() // 20, screen.get_height() // 20)
    #
    # massiv = [[random.choice([0, 1]) for j in range(3)] for i in range(3)]
    # print(massiv)
