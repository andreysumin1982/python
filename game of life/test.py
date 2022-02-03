import copy
import random
import time
#
n = 4
current_gen = [[random.randint(0,1) for j in range(4)] for i in range(n)]
#
next_gen=[[0 for j in range(4)] for j in range(n)]
#---
def findNeighbors(current_gen,x,y):
    # Ф-ция ищет соседей
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
            #print('Новая жизнь: ', 1)
            return 1
        else:
            return 0
#---
# import pygame
#
# pygame.init()
# width = 800
# height = 400
# screen = pygame.display.set_mode((width, height))
#
# mouse = pygame.image.load('mouse.png')
# #mouse = pygame.transform.rotate(mouse, 90)
#
# # Определяем стартовую позицию объекта
# mouseX = 0
# mouseY = 200
# # Задаем скорость движения объекта
# speed = 5
#
# while True:
#     screen.fill((70, 131, 94))
#     pygame.time.delay(30)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#     # Изменяем значение координаты Y
#     mouseX += speed
#     if mouseX > width:
#         mouseX = -50
#
#     screen.blit(mouse, (mouseX, mouseY))
#     pygame.display.update()
#--
class File():

    def __init__(self, path):
        self.path = path

    def readFile(self):
        with open (self.path) as file:
            for gen in file.readlines():
                yield gen

    def ipSearch(self, stroka, ip):
        self.stroka = stroka
        self.ip = ip
        if stroka.startswith(str(ip)):
            return stroka

#
f = File('/home/asumin/Документы/Программирование_Python/Для парсинга/access.log')
count = 0
ip = input('ip: ')
for i in f.readFile():
    if f.ipSearch(i, ip):
        print(i)
        count +=1
print(count)