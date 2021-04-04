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
#---------------------------------------------------------------
print('-'*30)
print(getattr(pt, "y", 'Такого значения нет.')) # Возвр. значен. атрибута, а если нет, выводит текст.
print(hasattr(pt, "i")) # Проверяет на наличии атрибута.
setattr(pt, "c", 122) # Задает значение атрибута, если его нет, то создает его.
print(pt.__dict__) # Выводит все атр. в экземпляре класса
print(pt.__doc__) # выводит строку с описанием класса, если нет ()
print(Point3D.__name__) # выводит имя класса
print(isinstance(pt, Point3D)) # проверяет принадлежность объекта к классу.

