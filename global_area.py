'''
Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.
Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.
Файл состоит из набора строк, каждая из которых представляет собой три поля:
Класс Фамилия Рост
Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.
Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.
В качестве ответа прикрепите файл с полученными данными о среднем росте.
'''
#---
'''
with open('/home/asumin/Загрузки/dataset_3380_5.txt', 'r', encoding='utf-8') as file: # read file
    arr = [[j for j in i.strip().split() ] for i in file.readlines()]
    # создаем 2d массив [['6', 'Tracey', '155'],['3', 'Lewin', '140'],....]
    print(arr)
#---
dict_medium = {}
for i in arr:
    dict_medium[i[0]] = dict_medium.setdefault(i[0], 0) + int(i[2])
print(dict_medium)
#---
dict_count = {}
dict_count2 = {}
for i in arr:
    if i[0] not in dict_count2:
        dict_count2[i[0]] = [1, int(i[2])]
    else:
        dict_count2[i[0]][0] += 1
        dict_count2[i[0]][1] += int(i[2])
    count = 0
print(dict_count2)
for i in range(1, 12):
    if str(i) not in dict_count2.keys():
        print(i,'-')
    else:
        print(i, (dict_count2[str(i)][1]/dict_count2[str(i)][0]))'''
#----------------------------------------------------------------------------------------------------------
'''Реализуйте программу, которая будет эмулировать работу с пространствами имен. 
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
-----------------------------------------------------------------------------------------------------------
Вашей программе на вход подаются следующие запросы:
    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> 
            внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> 
            при запросе из пространства <namespace>, или None, если такого пространства не существует
 Во пример вложенных пространств имено global, foo, bar:

namesp = {
    'global': {
        'parent': None,
        'vars': set('a'),
        'foo': {
            'parent': 'global',
            'vars': set('b'),
            'bar': {
                'parent': 'foo', 
                'vars': set('a')}
        }
    }
}

2. Количество команд считывал через n = int(input()). Затем в цикле while n != 0 считывал команды, 
сразу деля их на 3 переменные cmd, nmsp, var = input().split() и в зависимости 
от if cmd == я выполнял ту или иную функцию и передавал в нее остальные 2 переменные nmsp и var.
3. У меня было 3 основные функции 
- def get(namespace, var),
- def add(namespace,var),
    a['vars'].add(var)
- def create(namespace, parent)
    a[namespace] = {'parent':parent, 'vars':set()}
4. Для создания окружения я использовал рекурсивную функцию, 
которая ищет ключ словаря который будет родительским пространством для нового.

def finditem(obj, key):
    if key in obj:
        return obj[key]

5. Для поиска переменных я создал рекурсивную функцию 

def findvar(obj, namespace, var):
    if namespace in obj:
        if var in obj[namespace]['vars']:
            return namespace
--------------------------------------------------------------------------
или 2d массив [global, var, parrent]
              [ ...   ...    ....  ]
'''
#--
dg = {'global':
          {'parrent':None, 'vars': set(),
           'foo':{'parrent':'global', 'vars':set(),
                  'bar':{'parrent':'foo', 'vars':set()}}} }
#--
arr_keys = ['global'] #   ключи для словаря
#arr_vars = ['global']         #   переменные
#--      Ф-ция для добавл. vasr в словарь
def add_var(namespace, var):
    if var  not in d[namespace]['vars']:
        d[namespace]['vars'] = []
        d[namespace]['vars'].append(var)
    else: d[namespace]['vars'].append(var)
    print(d)
#--
def create_def(arr_keys):
    d={}
    count = 0
    for i in arr_keys:
        if i =='global':
            d[i] = {}
            d[i]['parrent'] = None
        elif name not in d:
            d[i] = {}
            d[i]['parrent'] = arr_keys[count]
            count+=1
    print(d)
#--
def get(namespace, var):
    pass
#--

#--  основное тело программы ---
n = 2
for i in range(n):
    command, name, namespace = input('<:').split()
    if command == 'add':
        pass
        #add_var(name, namespace)
    elif command == 'create':
        arr_keys.append(name)
        print(arr_keys)
        create_def(arr_keys)

#--
aw = {str(a + 1) + ' may':a for a in range(5)}
