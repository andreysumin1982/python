import copy
import pygame as p
import random


#
class Life():
    def __init__(self):
        pass

    def findNeighbors(self, current_gen, x, y):
        # Ф-ция ищет соседей
        # в пустой клетке, рядом с которой ровно 3 живые клетки, зарождается жизнь
        # если у живой клетки есть 2 или 3 живых соседки, то эта клетка продолжает жить
        # если у живой клетки меньше 2 или больше 3 живых соседки, клетка умирает
        self.current_gen = current_gen
        self.x = x
        self.y = y
        count = 0
        for iY in range(y - 1, y + 2):  # цикл от 0 до 3(не включая 3)
            for jX in range(x - 1, x + 2):  # цикл от 0 до 3(не включая 3)
                # print(current_gen[iY][jX], end=', ')
                if current_gen[iY][jX] == 1:
                    count += 1
        if current_gen[y][x] == 1:  # Если проверяемый элем. == 1
            count -= 1
            if count == 2 or count == 3:
                return 1
            else:
                return 0
        else:
            if count == 3:
                # print('Новая жизнь: ', 1)
                return 1
            else:
                return 0
#
class Game():
    '''Класс Game:
    * Инициализирует импортируемый модуль pygame
    * Создает игровое окно и отрисовывает логику класса Life'''
    def __init__(self):
        # init, запускает pygame.
        p.init()
        self.setColor()

    def setWindow(self, width, height, fps=60):
        # Игровое окно, задаем его размеры и fps.
        self.width = width
        self.height = height
        self.fps = fps
        # Игровое окно
        self.screen = p.display.set_mode((width, height))
        self.clock = p.time.Clock().tick(fps)

    def Generations(self):
         # Создаем двумерный массив и заполняем его (0,1) в случ. порядке
         self.current_gen = [[random.randint(0, 1) for j in range(self.width // 20)] for i in range(self.height // 20)]
         # Создаем двумерный массив для след. поколения, и заполняем  (0)
         self.next_gen = [[0 for j in range(self.width // 20)] for j in range(self.height // 20)]

    def setColor(self):
        # Цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

    def drowGrid(self, gridScreen, gridColor):
        # Сетка,
        self.gridScreen = gridScreen
        self.gridColor = gridColor
        #
        for i in range(0, self.height // 20):
            p.draw.line(self.screen, gridColor, (0, i * 20), (self.width, i * 20))
            #
        for j in range(0, self.width // 20):
            p.draw.line(self.screen, gridColor, (j * 20, 0), (j * 20, self.height))

    def drowRectangle(self, rectColor, rectScreen, x,y):
        # Прямоугольник
        self.rectColor = rectColor
        self.rectScreen = rectScreen
        self.x = x
        self.y = y
        p.draw.rect(rectScreen, (rectColor), (x * 20, y * 20, 20, 20))

    def run(self):
        # Экземпляр класса Life
        life = Life()
        # Бесконечный цикл
        while True:
            for event in p.event.get():  # смотрим события
                if event.type == p.QUIT:  # p.QUIT код: 256 - exit
                    exit(0) # Выход
                else:
                    # Закрашиваем окно
                    self.screen.fill(self.WHITE)
                    # Рисуем сетку под размер окна
                    self.drowGrid(self.screen, self.BLACK)
                    # Бежим по массиву
                    for x in range(1, (self.width // 20) - 1):
                        for y in range(1, (self.height // 20) - 1):
                            # Рисуем только живые клетки
                            if self.current_gen[y][x] == 1:
                                self.drowRectangle(self.GREEN, self.screen, x, y)
                            # Проверяем каждую клетку на наличие соседей и переносим ее в массив(следующее поколение)
                            self.next_gen[y][x] = life.findNeighbors(self.current_gen, x, y)
                    # После проверки всех клеток, копируем полученный массив (следующего поколения), и присваиваем переменную current_gen.
                    self.current_gen = copy.deepcopy(self.next_gen)
                    print(id(self.current_gen))
                    # После отрисовки, обновляем экран
                    p.display.update()
#
#
if __name__ == '__main__':
    # Экземпляр класса Life
    life = Life()
    # Экземпляр класса Game
    game = Game()
    # Создаем игровое окно
    game.setWindow(1900,800,60) #
    # Создаем текущее поколение
    game.Generations()
    # Запускаем игру
    game.run()
    
