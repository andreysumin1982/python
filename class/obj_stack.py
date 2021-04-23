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
p.sum()
print(p)
p.mul()
print(p)
