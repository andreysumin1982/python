import random
import time
#
n = 4
current_gen = [[random.randint(0,1) for j in range(n)] for i in range(n)]
#
next_gen=[[0 for j in range(n)] for j in range(n)]
#
def findNeighbors(current_gen, x,y):
    # Ф-ция ищет соседей
    count = 0
    for i in range(y-1, y+2): # цикл от 0 до 3(не включая 3)
        for j in range(x-1, x+2): # цикл от 0 до 3(не включая 3)
            if current_gen[i][j]:
                count +=1
        if current_gen[y][x]:
            count -=1
            if count ==2 or count == 3:
                return 1
            else:
                return 0
        else:
            if count ==3:
                return 1
            else:
                return 0
# Выводим матрицу
for k in current_gen:
    print(k)
print(20*'-')
#   0 0 0
#   0 1 0
#   0 0 0
# Циклом идем от 1 до предпоследнего элемента
for i in range(1, len(current_gen)-1):
    print('i: ',current_gen[i])
    for j in range(1, len(current_gen)-1):
        print('j: ',current_gen[i][j])
        print('Соседи: ', findNeighbors(current_gen, i,j))
