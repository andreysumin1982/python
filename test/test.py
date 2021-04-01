'''Этот файл предназначен для тестирования ф-ций, отдельного блока, объектов и т.д '''
#----
'''Задача global area. упрощеный вариант !'''
#
dict_namespace = {'global':{'parrent':'None','var':[]}} #
#
def get(namsp, var):      # передаем параметры (ключ, переменную)
    if namsp == 'None':   # namsp - это ключ в словаре или x[1] в списке.
        return namsp      # если он None, return
    elif var in dict_namespace[namsp]['var']: # var - пременная в словаре 'var':[]
        return namsp
    else: return get(dict_namespace[namsp]['parrent'], var) # если нет, тогда в качестве namsp передаем [namsp]['parrent'] - это родитель.
#
def body(): # Тело программы
    for x in [input('input: ').split() for cmd in range(int(input('n: ')))]: # !! Коротко и красиво генератор создает 2d массив и в цикле читает элементы.
        print(x)                                    # Выводи элемент ['','','']
        if x[0] == 'create':                        # идем по элементам и сравниваем
            dict_namespace[x[1]] = {'parrent': x[2], 'var':[]}  # добавляем в словарь
        elif x[0] == 'add':                         # повтор см. выше
            dict_namespace[x[1]]['var'].append(x[2]) #
        elif x[0] == 'get':                         # повтор см. выше
            print(get(x[1],x[2]))                   # вызыв. ф-цию get() и передаем ей параматры
#
#body()
print(dict_namespace)
#-----------------------------------------------------------------------------




