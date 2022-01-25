import random
import time
#
matrix = [
    [0,1,0],
    [0,0,0],
    [0,1,0]
]
x,y = 1,1
#--

for i in matrix:
    i.insert(0,0)
    i.insert(0,0)
    i.append(0)
    i.append(0)
#--
mass = [0 for i in range(0, len(matrix[0]))]
matrix.insert(0, mass)
matrix.insert(0, mass)
matrix.append(mass)
matrix.append(mass)
#print(matrix)
for i in matrix:
    print(i)

#-------------------------------------------
def summaryNeighbors(x,y):
    count = 0 # это счетчик
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0): #
                pass
            else:
                if (matrix[x + i][y + j] == 1):
                    count+=1
    return count # возвращаем число соседей
#-----------------------------------------

#
def calc_neighbors(x,y):
    count = 0 # счетчик
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j ==0:
                continue
            #print('i: ', i, 'j: ', j)
            #if is_alive(x+i, y+j):
                count+=1
    return count
#
def calc_gen(generation):
    new_generation = list() # список с новым поколением
    for (x,y) in generation:
        print(x,y)
        print(calc_neighbors(x,y))
        print(20 * '-')
        calc_n = calc_neighbors(x,y)
        if calc_n >=2 and calc_n <=3:
            new_generation.append((x,y))
    return new_generation
#
def run():
    #
    while True:
        print(calc_gen())
        time.sleep(4)

#
if __name__ == '__main__':

    print(summaryNeighbors(1,1))

    # massiv = [[j for j in range(4)] for i in range(4)]
    # print(massiv)
    # for i in massiv:
    #     for j in i[1:-1]:
    #         print(j)

    #run()
