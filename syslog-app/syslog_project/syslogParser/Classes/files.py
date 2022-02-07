import re
#--
class File():

    def __init__(self, path):
        self.path = path

    def readFile(self):
        with open (self.path) as file:
            for gen in file.readlines():
                yield gen

    def searchIp(self, stroka, ip):
        self.stroka = stroka
        self.ip = ip
        if stroka.startswith(str(self.ip)):
            print(stroka)

    def findSymbols(self, element, symbols):
        self.element = element
        self.reg_exp = re.compile(r'\b{}'.format(symbols))  # шаблон для поиска
        if re.findall(self.reg_exp, element): # если шаблон есть в строке
            print(element)

    def showFile(self):
        for stroka in self.readFile():
            print(stroka)
#--
#path = '/home/asumin/Документы/Программирование_Python/Для парсинга/syslog.txt'
path = '/home/asumin/Документы/Программирование_Python/Для парсинга/u_ex210730_log.txt'

#--
if __name__ == '__main__':
    pass
    #
    # file = File(path)
    # for elem in file.readFile():
    #     file.findSymbols(elem, 'VNIIRA-')