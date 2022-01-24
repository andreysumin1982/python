import random
#
def neighbors():
    # Ф-ция ищет соседей
    massiv = [[random.choice([0, 1]) for j in range(4)] for i in range(4)]
    #
    for k in massiv:
        print(k)
    print(20*'-')
    #
    new_massiv1 = [[j for j in massiv[i]] for i in range(1, len(massiv)-1)]
    print(new_massiv1)
    #
    elements = []
    #
    for i in range(0, len(new_massiv1)):
        for j in range(0, len(new_massiv1[i])):
            print(new_massiv1[i][j])

            #for l in range(0, len(new_massiv1[j])):
        print()


#
neighbors()