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
'''ООП'''
#
class Car:          # Создаем класс Car
    count = 0
    def __init__(self, a):
        self.a = a
        print('Create obj')
        Car.count += 1  # Счетчик
        print(Car.count)

    #def __init__(self, name, make, model): # __init__  Конструктор класса
    #    self.name = name
    #    self.make = make
    #    self.model = model
    #name = ''       # Атрибут класса имя
    #make = ''       # Атрибут класса
    #model = 2000    # Атрибут класса
    '''Создаем методы класса'''
    def start(self):    # Метод start
        print('Заводим машину.')
    def stop(self):     # Метод stop
        print('Стоп машина.')
    def run(self):      # Метод run
        print('Поехали.')
        #Car.count += 1  # Счетчик
        #print(Car.count)
#
#car_a = Car('Машина', 'Жига', 'ВАЗ2115') # Создаем объект (экземпляр класса) класса Car под названием car_a
#car_b = Car('Машина', 'BMW', '525')      # Создаем объект (экземпляр класса) класса Car под названием car_b
car_a = Car(1)
car_a.stop()
car_b = Car(2)
car_c = Car(3)
car_c.count = 100
print(car_c.count)
#
car_a.start()       # вызываем метод start() через объект car_a
#
car_a.run()
#Car.count = 2
#print(Car.count)
#print(car_c.count)
car_a.run()
#print(car_a.model)  # Получаем доступ к атрибуту класса Car

#-------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self, val=0):
        self.val = val
#
    def add(self, x):
        self.val += x
#
    def print_val(self):
        print(self.val)
#
a = A()
b = A(2)
c = A(4)
a.add(2)
b.add(2)
#
a.print_val()
b.print_val()
c.print_val()