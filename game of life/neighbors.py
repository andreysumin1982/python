import random
import time
#
massiv = [[random.choice([0, 1]) for j in range(4)] for i in range(4)]
# Инициализация точек
initial = [(3, 2), (3, 3), (2, 3), (3, 4), (4, 4)]
#
def calc_gen(generation):
    new_generation = list() # список с новым поколением
    for (x,y) in generation:
        new_generation.append((x,y))
        pass
    return new_generation
#
def run():
    #
    while True:
        print(calc_gen(initial))
        time.sleep(2)
#
if __name__ == '__main__':
    run()
