import random
import time
#
# matrix = [
#     [0,1,0],
#     [0,0,0],
#     [0,1,0]
# ]
# x,y = 1,1
# #--
#
# for i in matrix:
#     i.insert(0,0)
#     i.insert(0,0)
#     i.append(0)
#     i.append(0)
# #--
# mass = [0 for i in range(0, len(matrix[0]))]
# matrix.insert(0, mass)
# matrix.insert(0, mass)
# matrix.append(mass)
# matrix.append(mass)
#print(matrix)

#--
#--

# Ф-ция создает матрицу n x n
matrix = [[random.randint(1,1) for j in range(3)] for i in range(3)]
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
print('Исходная матрица')
for i in matrix:
    print(i)
print(30*'-')
#
matrixZero = [[0 for j in range(0, len(matrix))] for i in range(0, len(matrix))]

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
# def findNeighbors(x, y, matrix):
#     # Ф-ция ищет соседей
#     count = 0 # это счетчик
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if (i == 0 and j == 0): #
#                 pass
#             else:
#                 if (matrix[x + i][y + j] == 1):
#                     count+=1
#     return count # возвращаем число соседей
# #--

#
# def calc_neighbors(x,y):
#     count = 0 # счетчик
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j ==0:
#                 continue
#             #print('i: ', i, 'j: ', j)
#             #if is_alive(x+i, y+j):
#                 count+=1
#     return count
#
# def calc_gen(generation):
#     new_generation = list() # список с новым поколением
#     for (x,y) in generation:
#         print(x,y)
#         print(calc_neighbors(x,y))
#         print(20 * '-')
#         calc_n = calc_neighbors(x,y)
#         if calc_n >=2 and calc_n <=3:
#             new_generation.append((x,y))
#     return new_generation


    # в пустой клетке, рядом с которой ровно 3 живые клетки, зарождается жизнь
    # если у живой клетки есть 2 или 3 живых соседки, то эта клетка продолжает жить
    # если у живой клетки меньше 2 или больше 3 живых соседки, клетка умирает


#--
def run():
    #
    #count = 0
    #while True:
        #if count < len(matrix)-2:
            # Выводим матрицу
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            ncount = findNeighbors(i,j,matrix)
            print(i,j, 'Соседи: ->', ncount)
            # если в пустой клетке, рядом с которой ровно 3 живые клетки, зарождается жизнь
            #print(findNeighbors(i, j, matrix))
            if ncount == 3:
                matrixZero[i][j] = 1
                # если у живой клетки есть 2 или 3 живых соседки, то эта клетка продолжает жить
            elif matrix[i][j] == 1 and (ncount == 2 or ncount ==3):
                matrixZero[i][j] = matrix[i][j]
            # если у живой клетки меньше 2 или больше 3 живых соседки, клетка умирает
            elif (ncount < 2 or ncount > 3):
                matrixZero[i][j] = 0
                #print('*', findNeighbors(i,j,matrix))
                #print(findNeighbors(i,j,matrix))
        time.sleep(0)



    print(30 * '-')
    for i in matrixZero:
        print(i)
    print(30 * '-')

#--
if __name__ == '__main__':
    #
    run()

    #print(findNeighbors(1,1))
