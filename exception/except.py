'''Задачи stepic.org.  Ошибки и исключения

Вашей программе будет доступна функция foo, которая может бросать исключения.
Вам необходимо написать код, который запускает эту функцию,
затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError
и выводит имя пойманного исключения.'''
def foo():
    pass
try:
    foo()
except ZeroDivisionError:   # Выводим в порядке наследования  (ZeroDivisionError.mro())
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print("AssertionError")
#-------------------------------------------
#PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Исключения/test'
PATH = '/home/asumin/Документы/Программирование Python/Stepic.org/Основы и применение/Исключения/test'
#
def read_file(p):
    with open(p) as file:
        return [i.strip().split(':') for i in file.readlines()]
#
r = read_file(PATH) # ф-ция. read_file(PATH) возвр. список [[''],['']]
dict_class = {} # добавл. в словарь предка и наследника
#
def add_dict(p):
    for i in range(1, int(p[0][0])+1):
        if len(p[i]) == 1:
            dict_class[p[i][0]] = 'None'  # Убираем пробелы, доводим до состояния {'..':'..'}
        else:
            dict_class[p[i][0].strip()] = ''.join(p[i][1:]).strip().split() # Убираем пробелы, доводим до состояния {'..':'..'}
    print(dict_class)
#
add_dict(r)
#
k = int(r[0][0])+2 # для среза
arr = [''.join(i) for i in r[k:]] # получаем список из запросов.
print(arr)
#
dk = [i for i in dict_class.keys()] # Получаем список ключей
#print(dk)
#
def rec(parr, arr_dk): # Создаем рекурсию
    if len(arr_dk) == 0:
        return []
    if dict_class[parr] != 'None' or parr in dict_class[parr]:
        return parr
    else: rec(parr, arr_dk[1:])
    return []

def request(p): # бежим по списку запросов [arr]
    for i in p:
        print(rec(i, dk))
request(arr)
#--------------- Реализация для stepic.org-----------------
'''def recur(arr_parr):
    if len(arr_parr) == 0:
        return
    k = arr_parr[0]
    if k in di[k]:
        return k
    else:
        recur(arr_parr[1:])

#
di = {}
s = set()
for i in [input('>').strip().split(':') for j in range(int(input('n1: ')))]:
    if len(i) == 1:
        di[i[0].strip()] = 'None'
    else:
        di[i[0].strip()] = ''.join(i[1:]).strip().split()
print(di)
#
arr_req = []
for i in [input('<').strip().split() for j in range(int(input('n2: ')))]:
    arr_req.append(''.join(i))
print(arr_req)
#
print(recur(arr_req))
#'''