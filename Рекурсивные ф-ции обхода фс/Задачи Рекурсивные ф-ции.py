'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса,
и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и
выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2
#--------------------------------------------------
with open('/home/asumin/Загрузки/dataset_3380_5.txt', 'r', encoding='utf-8') as file: # read file
    arr = [[j for j in i.strip().split() ] for i in file.readlines()]
    # создаем 2d массив [['6', 'Tracey', '155'],['3', 'Lewin', '140'],....]
    print(arr)
#---
dict_medium = {}
for i in arr:
    dict_medium[i[0]] = dict_medium.setdefault(i[0], 0) + int(i[2])
print(dict_medium)
#--------------------------------------------------

'''
import json
import sys
#
path_file = "/home/asumin/Документы/Программирование Python/stepik.org/Основы и применение/csv_json-файлы/Parrents.json"
#
dict_list = {} # словарь такого типа {'B': {'parrents': ['A', 'C']}, 'C': {'parrents': ['A']},...}
#
def read_json(path):
    with open(path) as file:
        f = json.load(file) #  получаем список из словарей.
    for j in f:
        if j['name'] not in dict_list:
            dict_list[j['name']] = {}
            dict_list[j['name']] = j['parents']
        else: dict_list[j['name']] += j['parents']
    print(dict_list) # созд словарь такого типа {'B': {'parrents': ['A', 'C']}, 'C': {'parrents': ['A']},...}
#
def f1(a, count = 0):
    if a in dict_list:
        count += 1
    for i in dict_list:
        if a in dict_list[i]:
            count +=1
    return count
#
#read_json(path_file)
#for i in dict_list:
#    print(f'{i} : {f1(i)}')
#-------------------------------Решение других----------------------------
with open(path_file) as f:  # чтоб не вводить, читаем из файла.
    data = json.load(f) # получили список из словарей.
# [{'name': 'B', 'parents': ['A', 'C']}, {'name': 'C', 'parents': ['A']}, }
#
child = {} # создаем словарь, чтобы добавлять туда -> {предок : [наследники,..]}
parents = {c['name']: c['parents'] for c in data} # получаем словарь такого типа {'B': ['A', 'C'], 'C': ['A'], }
print(parents)
#
def f2(x, y):
    for i in parents: # Бежим по словарю НЕ отсортир. {'B': ['A', 'C'], 'C': ['A'], }
        if y in parents[i]: # Если x (т.е. A) входит в B:['A', 'C']
            child[x].append(i) # A:[B] добавили наследника
            print(child)
            f2(x, i) # Рекурсия, передаем x->(A) и В. Т.е узнаем, есть ли еще наследики у родителя x(A)
#
for i in sorted(parents): # Бежим по отсортированному словарю (по ключам)
    child[i] =[] # создаем предка {i : []} с пустым списком наследников.
                 # {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}
                 # В рекурсивн. ф-ции будем добавлять туда наследников
    f2(i, i)
    print(i, ':', len(set(child[i]))+1)
#-----------------------------------------------------------------
'''Рекурсивная ф-ция для обход файлов.'''
import os
#
path = '/home/asumin/Загрузки'
file = 'STP Порты'
#
path_list = os.listdir(path) # Выводим содержимое папки в виде списка
#
for i in path_list:
    if os.path.isdir(f'{path}/{i}'): # Узнаем, каталог или файл ? (! передаем в isdir полный путь !)
        print(f'Каталог: {path}/{i}') # Выводим
    else: print(f'Файл:    {path}/{i}')  #
print(path_list)
#
'''Нужно найти файл STP Порты'''
#
def obhodDir(p, f):
    for i in os.listdir(p):
        if f in os.listdir(p):
            return print(f'Нашли: {p}/{file}')
        else:
            if os.path.isdir(f'{p}/{i}'):
                #print(f'Спускаемся в {p}/{i}')
                obhodDir(f'{p}/{i}', f) # Вызываем рекурсивно, передавая путь, куда переходить и искать файл.
                #print(f'Возвращаемся на {p}')
#
#obhodDir(path, file)
#------------------------------------------------
def f3(x): # сложение чисел от 1 до n
    if x == 0:
        return 0
    return x + f3(x-1)
#print(f3(3))
#------------------------------------------------
def f4(p):  # Перебираем список рекурсией
    if len(p) == 0:
        return
    print(p[0])
    return f4(p[1:])
#f4(path_list)
#------------------------------------------------
def obhodDir2(p):
    print(os.listdir(p))
    #for i in os.listdir(p):
    #    print(i)
#obhodDir2(path)


