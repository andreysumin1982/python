'''stepic.org, тесты, задачи на тему ООП'''
#------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------
class Hero():
    '''Класс создаем героя для игры'''
    def __init__(self, name, race, level, force, magic, intelligence):
        self.name = name
        self.race = race
        self.level = level
        self.force = force
        self.magic = magic
        self.intelligence = intelligence
    '''Добавляем методы'''
    def name(self):
        pass
    def race(self):
        pass
    def level(self):
        pass
    def force(self):
        pass
    def magic(self):
        pass
    def intelligence(self):
        pass
#----------------------------------------
class Point3D():
    '''Класс для хранения координат'''
    arr_xy = [] # Для хран. координат
    def __init__(self, coordinat = None):
        self.coordinat = Point3D.arr_xy.append(coordinat)
pt = Point3D(123)
print(Point3D.arr_xy)
class Point(Point3D):
    '''Дочерний класс '''
    def __init__(self, coordinat = 0):
        self.coordinat = Point3D.arr_xy.append(coordinat)
pt1 = Point('erwer')
print(Point3D.arr_xy)
#--
#------------------------------------------------------------------------------------
class MoneyBox():
    '''Класс копилка задание stepic.org'''
    list_box = [] # список для добалнения значений
    def __init__(self, capacity): # Конструктор. вх. значение вместительность list_box
        self.capacity = capacity
        self.count = 0
    #
    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        return False
    #
    def add(self, v):
        if self.can_add(v):
            self.count += v
#
x = MoneyBox(10)
x.add(5)
x.add(3)
x.add(0)
print(x.can_add(2))
#print(x.can_add(2))
#-
print(x.capacity)
print('*'*20)
#-------------------------------------------------------------------------------------
class Buffer:
    '''Класс Buffer, задание stepic.org'''
    def __init__(self):
        self.list = []
    '''Метод добавления элементов. в список и вывод.'''
    '''def add(self, *a):
        for i in a: self.list.append(i)   # Добавляем в список
        #print(self.list)
        while len(self.list) >= 5:  # Пока длинна >= 5 выполняем...
            summa = 0; count = 0    # Сумма, счетчик элементов.
            for i in self.list:     # Бежим по списку.
                summa += (i); count +=1 # Подсчитываем сумму и счетчик
                if count == 5:
                    print(summa)
                    for j in self.list[:count]: # Отсекаем первую пятёрку элементов
                        self.list.remove(j)
                    i, j = 0, 0      # Обнуляем сумму, счетчики циклов.
                    #print(self.list)'''
    ''' !! Более улучшенный метод добавления и посчета'''
    def add(self,*a):
        for i in a:    # Бежим по кортежу
            self.list.append(i) # Добавляем в список
            if len(self.list) == 5: # если длинна списока составила 5 элем.
                print(sum(self.list))  # Выводим сумму всех элементов
                self.list.clear() # Очищаем список из 5 елементов, и возвращ. в начало цикла
    '''Вернуть сохраненные в текущий момент элементы последовательности в порядке, 
    в котором они были добавлены'''
    def get_current_part(self):
        #if len(self.list) < 5:
        return self.list
#-
b = Buffer()
#b.add(*range(42**4))
#print(b.get_current_part())
#------------------------------------------------------------------------------------
'''Тестируем map, lambda'''
lst = [*range(1,150001)]
def sqr_func(iter):
    return (iter*2)//2**5
def run():
    m = list(map(sqr_func, lst))
    return m
print(run())
'''---------------------------'''






#---------------------------------------------------------------
print('-'*30)
print(getattr(pt, "y", 'Такого значения нет.')) # Возвр. значен. атрибута, а если нет, выводит текст.
print(hasattr(pt, "i")) # Проверяет на наличии атрибута.
setattr(pt, "c", 122) # Задает значение атрибута, если его нет, то создает его.
print(pt.__dict__) # Выводит все атр. в экземпляре класса
print(pt.__doc__) # выводит строку с описанием класса, если нет ()
print(Point3D.__name__) # выводит имя класса
print(isinstance(pt, Point3D)) # проверяет принадлежность объекта к классу.
#---------------------------------------------------------------