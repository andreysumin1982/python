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