'''Задача на stepic: Реализуйте структуру данных, представляющую собой расширенную структуру стек.
Необходимо поддерживать добавление элемента на вершину стека,
удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления. '''
class ExtendedStack(list):
    def sum(self):
        # операция сложения
        s = self.pop() + self.pop()
        self.append(s)
    def sub(self):
        # операция вычитания
        s = self.pop() - self.pop()
        self.append(s)
    def mul(self):
        # операция умножения
        s = self.pop() * self.pop()
        self.append(s)
    def div(self):
        # операция целочисленного деления
        s = self.pop() // self.pop()
        self.append(s)
p = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
#p.sum()
#print(p)
#p.mul()
#print(p)
#-------------------------------------------------------------------------
'''Задача stepic.org: Реализуйте класс LoggableList, 
отнаследовав его от классов list и Loggable таким образом, 
чтобы при добавлении элемента в список 
посредством метода append в лог отправлялось сообщение, 
состоящее из только что добавленного элемента.'''

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list, Loggable):
    def append(self, name):
        super().append(name)
        self.log(name)
        #print(self)
d = LoggableList([1, 2, 3, 4, -3, 3, 5, 10])
d.append(200)