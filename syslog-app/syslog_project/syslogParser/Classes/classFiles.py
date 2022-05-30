import re
import os
import zipfile
#--
class File():
    #
    def __init__(self, path):
        self.path = path
    #
    def readFile(self):
        with open (self.path) as file:
            for gen in file.readlines():
                yield gen
    #
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
    #
    def extractZip(self):
        fileZip = f'{pathZipFiles}/{self.path}' # абсолютный путь к zip-файлу
        absPathExtractFile = f'{fileZip.strip(".zip")}/{self.path.replace(".zip", ".txt")}' # абсолютный путь к распакованному файлу
        if os.path.isfile(absPathExtractFile): # если файл распакован, возвращаем путь
            print(f"Файл уже распакован: {absPathExtractFile}")
            return absPathExtractFile
        else:
            print(f"Распаковываю {self.path} в папку: {fileZip.strip('.zip')}")
            z = zipfile.ZipFile(fileZip) #
            z.extractall(fileZip.strip('.zip')) # Распаковываем в папку(имя файла)
            #extractedFile = os.listdir(os.path.join(fileZip.strip(".zip")))
            extractedPathDir = f'{fileZip.strip(".zip")}/{self.path.replace(".zip", ".txt")}'#f"{fileZip.strip('.zip')}/{''.join(extractedFile)}" # Абсолютный путь к распакованному файлу
            return extractedPathDir
    #
    def searchIp(self, stroka, ip):
        self.stroka = stroka
        self.ip = ip
        if stroka.startswith(str(self.ip)):
            print(stroka)
    #
    def findSymbols(self, element, symbols):
        #self.element = element
        reg_exp = re.compile(r'\b{}'.format(symbols), flags=re.IGNORECASE)  # шаблон для поиска с игнором на регистр
        if re.findall(reg_exp, element): # если шаблон есть в строке
            return element
    #   
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