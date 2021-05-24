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
   p = read_file(PATH)[0].split(' ')
   p2 = read_file(PATH)[1].split(' ')
   #
   year = int(p[0])
   month = int(p[1])
   day = int(p[2])
   #
   p_days = int(p2[0])
   p_date = datetime.date(year, month, day)
   delta = datetime.timedelta(p_days)
   p_date += delta

   print(p_date.strftime("%Y %m %d").replace(' 0', ' '))
run()
#------ Реализация для Stepic (Simple in / out )----------

p_date = input(': ').split()
p_days = int(input(': '))
#
year = int(p_date[0])
month = int(p_date[1])
day = int(p_date[2])
#
p_date = datetime.date(year, month, day)
delta = datetime.timedelta(p_days)
p_date += delta
#
print(p_date.strftime("%Y %m %d").replace(' 0', ' '))