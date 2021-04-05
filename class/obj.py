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
class MoneyBox():
    '''Класс копилка'''
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
#-------------------------------------------------------------
class Buffer:
    '''Класс Buffer, задание stepic.org'''
    def __init__(self):
        self.count = 0
        self.list = []

    '''Обьявляем методы'''
    def add(self, *a): # Метод добавления эл. в список
        for i in a: self.list.append(' '.join(str(i)))
        print(self.list, '*')

    '''def get_current_part(self):
        s = 0
        for i in self.list:
            s +=i; self.count += 1
            if self.count == 5:
                self.list = None
                return s
        else: return self.list[:self.count]'''


b = Buffer()
b.add(1,2,3,4)
b.add(11)
b.add(12)
b.add(13)




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
