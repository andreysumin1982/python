'''Задачи stepic.org.  Модули и импорт'''
import module1
import module2

print(3)
#-------------------------------------------
import datetime
from datetime import timedelta
#
PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Модули/test'
#
def read_file(path_file):
    with open(path_file) as file:
        return [i.strip() for i in file.readlines()]
print(read_file(PATH))

def run():
    for i in read_file(PATH)[0].split(' '):
        print(i)

run()