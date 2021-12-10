# Импортируем модули
import paramiko
import re
import csv

# Файл со списком коммутаторов
pathFileSwitch = '/home/asumin/github/projects/stepic/Парсинг Cisco/iswitch'

# Файл для записи свободных портов
pathUnusedPorts = '/home/asumin/github/projects/stepic/Парсинг Cisco/unusedPorts'

# Параметры подключения
sshParams = {'host': '',
             'user': 'admin',
             'password': '*******',
             'port': '22'}

# Команды
commands = 'sh int counters' # для примера

# создаем ф-цию sshConnect
def sshConnect(host, user, password, port):
    # Ф-ция подкл по протоколу ssh и возвращает словарь с данными.
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port, look_for_keys=False, allow_agent=False)
    # Выполняем
    dictOutput = {'output': []} # добавляем в словрь вывод ф-ции "client.exec_command(commands)"
    stdin, stdout, stderr = client.exec_command(commands)
    dictOutput['output'] += (stdout.readlines() + stderr.readlines())
    #print(dictOutput) # Смотрим listOutput
    # Закрываем соединение
    client.close()
    return dictOutput

# Смотрим вывод sshConnect и сохраняем в файл unusedPorts
def showData(data):
    # Словарь для неиспользуемых портов коммутатора
    unusedPorts = {'counters': 0, 'unusedPorts': []}
    reg_exp = re.compile(r'\b\w{4}0\b')  # шаблон для поиска (найти строки где есть 0, 0, 0, 0)
    for value in data['output']:
        #print(value, value.find('0', 10))
        if re.findall(reg_exp, ''.join(value.split())):
            unusedPorts['counters'] += 1 # кол-во свободн . портов
            unusedPorts['unusedPorts'].append(value.split()[0]) # порты
    # Записываем в файл
    with open(pathUnusedPorts, 'w') as writeFile:
        #
        writeFile.write('Кол-во: '+str(unusedPorts['counters'])+'\n')
        for port in unusedPorts['unusedPorts']: #
            writeFile.write(port+'\n')
        print('Файл unusedPorts сохранен.')

# Смотрим список коммутаторов из файла
def getSwitch(path):
    with open(path) as file:
        for item in file.readlines():
            #print(item)
            sshParams['host'] = ''.join(item.split()) #Добавляем в словарь + отрезаем '\n'
            #print(sshParams)
            # Вызываем ф-цию sshConnect
            output = sshConnect(sshParams['host'], sshParams['user'], sshParams['password'], sshParams['port'])
            # Вызываем showData смотрим вывод
            showData(output)

#--------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # Вызываем ф-цию getSwitch
    getSwitch(pathFileSwitch)

