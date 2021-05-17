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
PATH = '/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/Исключения/test'
#PATH = '/home/asumin/Документы/Программирование Python/Stepic.org/Основы и применение/Исключения/test'
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
            dict_class[p[i][0]] = []  # Убираем пробелы, доводим до состояния {'..':[]}
        else:
            dict_class[p[i][0].strip()] = ''.join(p[i][1:]).strip().split() # Убираем пробелы, доводим до состояния {'..':['..']}
    print(dict_class)
#
add_dict(r)
#
k = int(r[0][0])+2 # для среза
arr = [''.join(i) for i in r[k:]] # получаем список из запросов.
print(arr)
#
def rec(parr): # Создаем рекурсию
    for p in dict_class[parr]:
        #print(f'{p} - p(i)')
        dk.add(p)
        rec(p)
#
def run():
    for i in arr: # идем по списку
        #print(f'{i} - i')
        global dk
        dk = set() # Обнуляем пустое множество
        rec(i) # Вызывем рекурсию и передаем ей итер. аргумент
        for j in dk:
            #print(f'{dk} - dk')
            if j in arr:
                print(f'{i} - Нашли' ); break
    #
run()
#--------------- Реализация для stepic.org-----------------
'''
Функции rec, run добавляем.
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
'''