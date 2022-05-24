import re
import os
#--
class File():

    def __init__(self, path):
        self.path = path

    def readFile(self):
        with open (self.path) as file:
            for gen in file.readlines():
                yield gen
    
    def readZipFiles(self):
        # Смотрим файлы в директории
        dirFiles =os.listdir(os.path.join(self.path))
        archFiles = {'name':[]}
        for file in dirFiles:
            #archFiles['fullPath'].append(f'{pathZipFiles}/{file}\n')
            if file.endswith('.zip'): # отбираем только *.zip
                archFiles['name'].append(f'{file}\n')
            continue
        return sorted(archFiles['name'])
    
    def extractZip(self):
        return self.path
    
    
    def searchIp(self, stroka, ip):
        self.stroka = stroka
        self.ip = ip
        if stroka.startswith(str(self.ip)):
            print(stroka)

    def findSymbols(self, element, symbols):
        self.element = element
        self.reg_exp = re.compile(r'\b{}'.format(symbols), flags=re.IGNORECASE)  # шаблон для поиска с игнором на регистр
        if re.findall(self.reg_exp, element): # если шаблон есть в строке
            return element
        
    def showFile(self):
        for stroka in self.readFile():
            print(stroka)
#--
path = '/home/asumin/Документы/Программирование_Python/Для парсинга/syslog.txt'
pathZipFiles = '/home/asumin/Документы/Программирование_Python/Для парсинга/syslog-zip'
#--
if __name__ == '__main__':
    pass
    #
    # file = File(path)
    # for elem in file.readFile():
    #     file.findSymbols(elem, 'VNIIRA-')