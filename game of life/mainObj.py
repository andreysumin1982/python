import copy
import pygame as p
import random
#
class Life:
    def __init__(self, matrix):
        self.matrix = matrix
    def findNeighbors(self):
        pass
    def nextGenerations(self):
        pass
    def getMatrix(self):
        return self.matrix
#
class Game():
    def __init__(self):
        # init запускает pygame.
        p.init()
        self.setColor()

    def setWindow(self, width, height, fps=60):
        # окно программы, задаем его размеры в настройках.
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = p.display.set_mode((width, height))
        self.clock = p.time.Clock().tick(fps)

    def setCaption(self, text):
        # заголовок окна
        self.text = 'Live'
        p.display.set_caption(str(text))

    def setColor(self):
        # Цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

    def drowGrid(self, gridScreen, gridColor):
        self.gridScreen = gridScreen
        self.gridColor = gridColor
        #
        for i in range(0, self.height // 20):
            p.draw.line(self.screen, gridColor, (0, i * 20), (self.width, i * 20))
            #
        for j in range(0, self.width // 20):
            p.draw.line(self.screen, gridColor, (j * 20, 0), (j * 20, self.height))

    def drowRectangle(self, rectColor, rectScreen):
        self.rectColor = rectColor
        self.rectScreen = rectScreen

    def run(self):
        # Запускаем игру
        self.setWindow(1600,800,60)
        print(self.screen)
        self.setCaption('Live')
        print(self.screen.fill(self.WHITE))
        while True:
            for event in p.event.get():  # смотрим события
                if event.type == p.QUIT:  # p.QUIT код: 256 - exit
                    exit(0)
                else:
                    self.screen.fill(self.WHITE)
                    self.drowGrid(self.screen, self.BLACK)
                    #
                    p.display.update()

#
if __name__ == '__main__':
    game = Game()
    game.run()
    #
    # # создаем игру и окно
    # p.init()  # init запускает pygame.
    # screen = p.display.set_mode((800, 800))  # окно программы, задаем его размеры в настройках.
    # p.display.set_caption("Жизнь")  # заголовок окна
    # clock = p.time.Clock()  # частота выполнения за одну секунду.
    # WIDTH = 1600  # ширина игрового окна
    # HEIGHT = 900  # высота игрового окна
    # FPS = 60  # частота кадров в секунду
    # #
    # # Цвета (R, G, B)
    # BLACK = (0, 0, 0)
    # WHITE = (255, 255, 255)
    # RED = (255, 0, 0)
    # GREEN = (0, 255, 0)
    # BLUE = (0, 0, 255)
    # while True:
    #     for event in p.event.get():  # смотрим события
    #         if event.type == p.QUIT:  # p.QUIT код: 256 - exit
    #             exit(0)
    #         else:
    #             screen.fill(WHITE)
    #             # Рисуем сетку под размер окна
    #             for i in range(0, HEIGHT // 20):
    #                 p.draw.line(screen, BLACK, (0, i * 20), (WIDTH, i * 20))
    #                 #
    #             for j in range(0, WIDTH // 20):
    #                 p.draw.line(screen, BLACK, (j * 20, 0), (j * 20, HEIGHT))
    #             # ----------------------------------------------------------------------------
    #             p.display.update()

#    def run1(self):
#     # создаем игру и окно
#     p.init()  # init запускает pygame.
#     screen = p.display.set_mode((800, 800))  # окно программы, задаем его размеры в настройках.
#     p.display.set_caption("Жизнь")  # заголовок окна
#     clock = p.time.Clock()  # частота выполнения за одну секунду.
#     WIDTH = 1600  # ширина игрового окна
#     HEIGHT = 900  # высота игрового окна
#     FPS = 60  # частота кадров в секунду
#     #
#     # Цвета (R, G, B)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     while True:
#         for event in p.event.get():  # смотрим события
#             if event.type == p.QUIT:  # p.QUIT код: 256 - exit
#                 exit(0)
#             else:
#                 screen.fill(WHITE)
#                 # Рисуем сетку под размер окна
#                 for i in range(0, HEIGHT // 20):
#                     p.draw.line(screen, BLACK, (0, i * 20), (WIDTH, i * 20))
#                     #
#                 for j in range(0, WIDTH // 20):
#                     p.draw.line(screen, BLACK, (j * 20, 0), (j * 20, HEIGHT))
#                 # ----------------------------------------------------------------------------
#                 p.display.update()