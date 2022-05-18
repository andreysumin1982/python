from netmiko import (ConnectHandler,
                     NetmikoTimeoutException,
                     NetmikoAuthenticationException)
from datetime import datetime
import time
import re
# Файл со списком коммутаторов
fileSwitch = 'switch'
# Параметры подключения к коммутаторам Cisco Catalyst
handlerCatalyst = {
    'device_type': 'cisco_ios',
    'host': '',
    'user': '*****',
    'password': '*****',
    'secret' : '*****'
    }
# Параметры подключения к коммутаторам Cisco SG300
handlerSG300 = {
    'device_type': 'cisco_s300',
    'host': '',
    'user': '*****',
    'password': '*****'
    }
# Команды
commands = ['sh int des', 'sh run int ', 'sh int config',
            'conf', 'int range gi ', 'int range Gi ']
# Вывод ф-ции sshConnect для всех коммутаторов
outputsshConnect = {}
# Вывод ф-ции sshConnect только для коммутаторов SG300
outputsshConnectSG300 = {}
# Вывод {'порт':[настройки порта]}
dictFSTEK = {}
# Вывод {'порт':[up/down]} для SG300
dictStatusPortSG300 = {}
# Список портов со статусом FSTEK
listAdminDown = []
# Имя коммутатора
listNameSwitch = []
# Таймер
timer = ''
def sshConnect(nameSwitch, ciscoHandler):
    reg_exp = re.compile(r'iSG|isg') # Шаблон поиска. Ищем SG или sg
    if re.findall(reg_exp, nameSwitch.strip()):
        try:                    # SG300 #
            start = datetime.now().replace(microsecond=0)
            with ConnectHandler(device_type = ciscoHandler['device_type'],
                                ip = ciscoHandler['host'],
                                username = ciscoHandler['user'],
                                password = ciscoHandler['password']) as ssh:
                # Выполняем
                time.sleep(1)  # Пауза
                output = ssh.send_command(commands[0]) # Вывод команды sh int des
                outputsshConnect['output'] = output.split('\n') # заносим в словарь
                time.sleep(1)
                output = ssh.send_command(commands[2]) # Вывод команды sh int config
                outputsshConnectSG300['output'] = output.split('\n') # заносим в словарь
            stop = datetime.now().replace(microsecond=0); timer = stop-start
            return dataAnalysier(nameSwitch, outputsshConnect, outputsshConnectSG300, timer)
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print('Error:', error); exit(0)
    else:
        try:                    # Catalyst #
            start = datetime.now().replace(microsecond=0)
            with ConnectHandler(device_type = ciscoHandler['device_type'],
                                ip = ciscoHandler['host'],
                                username = ciscoHandler['user'],
                                password = ciscoHandler['password'],
                                secret = ciscoHandler['secret']) as ssh:
                # Выполняем
                ssh.enable()
                time.sleep(1)  # Пауза
                output = ssh.send_command(commands[0]) # sh int des
                outputsshConnect['output'] = output.split('\n') # заносим в словарь
                ssh.exit_enable_mode()
            stop = datetime.now().replace(microsecond=0); timer = stop - start
            return dataAnalysier(nameSwitch, outputsshConnect, None, timer)
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print('Error:', error); exit(0)
#
def dataAnalysier(nameSwitch, dataOutput, dataOutputSG300 = None, timer = None):
    reg_exp_sg300 = re.compile(r'iSG|isg') # Шаблон поиска. Ищем iSG или isg
    reg_exp_fstek = re.compile(r'\bFSTEK\b') # Шаблон поиска.Ищем FSTEK
    listAdminDown.clear(); dictFSTEK.clear() # Чистим структуры данных
    if re.findall(reg_exp_sg300, nameSwitch.strip()):
        for it in dataOutputSG300['output']: #
            if 'gi' in it.strip():
                dictStatusPortSG300[it.split()[0]] = [it.split()[6]] # {port: up/down}
            continue
        for item in dataOutput['output']: #
            if 'gi' in item.strip() and re.findall(reg_exp_fstek, item.strip()):
                dictFSTEK[item.split()[0]] = item.split('\n') # Добавляем в словарь порт, description
                dictFSTEK[item.split()[0]] += dictStatusPortSG300[item.split()[0]] # Добавляем статус Down
                listAdminDown.append(item.split()[0]) # Добавляем только порты FSTEK
                print(''.join(item.split('\n')), ''.join(dictStatusPortSG300[item.split()[0]]))
            continue
        summaryPorts(listAdminDown, timer); listNameSwitch.append(nameSwitch)
        return dictFSTEK
    else:         #  ----------- Catalyst ------------ #
        reg_exp = re.compile(r'\bFSTEK\b') # Шаблон поиска. Ищем admin down
        for item in dataOutput['output']:
            if re.findall(reg_exp, item) and 'Gi' in item.split()[0]:  # отбираем только Gi порты "admin down"
                dictFSTEK[item.split()[0]] = item.split()
                listAdminDown.append(item.split()[0]) # Добавляем только порты
                print(item.split()[0], item.split()[1], " ".join(item.split()[3:])) #
            continue
        # dictFSTEK {'Gi0/1': ['Gi0/1', 'admin', 'down', 'down', 'FSTEK', 'OSK-1.2.04-13', 'room', '118'], 'Gi0/3': ['Gi0/3', 'admin', 'down', 'down', 'FSTEK', 'OSK-1.2.8.03', 'room', '117']}
        summaryPorts(listAdminDown, timer); listNameSwitch.append(nameSwitch)
        return dictFSTEK
#
def summaryPorts(ports, timer):
    # Ф-ция выводит сумму портов
    remainder = len(ports) % 10  #
    if len(ports) == 0:
        print(f'\nНайдено: {len(ports)} портов \nВремя поиска: {timer} \n' + '-' * 47 +'\n')
    elif (remainder == 0 or remainder >= 5 or (10 <= len(ports) <= 19)):
        print(f'\nНайдено: {len(ports)} портов \nВремя поиска: {timer} \n' + '-' * 47 +'\n')
    elif remainder == 1:
        print(f'\nНайдено: {len(ports)} порт \nВремя поиска: {timer} \n' + '-' * 47 +'\n')
    else:
        print(f'\nНайдено: {len(ports)} порта \nВремя поиска: {timer} \n' + '-' * 47 +'\n')
#
def splitArraySG300(outputData):
    # Ф-ция обрабатывает отсортированный массив
    # ['gi1', 'gi3', 'gi4', 'gi5', 'gi9', 'gi10', 'gi12', 'gi13'..]
    # и возвращает массив:
    # [[1], [3, 4, 5], [9, 10], [12, 13] ..]
    tempset = [[]]
    prew_item ,next_item = 0, 0
    for item in outputData:
        item = int(item.replace('gi', ''))
        if (next_item + 1) == item:
            tempset[prew_item].append(item)
            next_item = item
        else:
            tempset.append([item])
            prew_item +=1
            next_item = item
    if tempset[0] == []:
        tempset.remove(tempset[0])
    return tempset
#
def splitArrayCatalyst(outputData):
    # Ф-ция обрабатывает отсортированный массив
    # [2, 4, 6, 7, 8 ..]
    # и возвращает массив:
    # [[2], [4], [6, 7, 8], [48, 49, 50, 51]]
    tempset = [[]]
    prew_item ,next_item = 0, 0
    for item in outputData:
        if (next_item + 1) == item:
            tempset[prew_item].append(item)
            next_item = item
        else:
            tempset.append([item])
            prew_item +=1
            next_item = item
    if tempset[0] == []:
        tempset.remove(tempset[0])
    return tempset
#
def splitDictCatalyst(outputData):
    # Ф-ция обрабатывает отсортированный массив
    #['Gi1/0/2', 'Gi1/0/4', 'Gi1/1/6', 'Gi1/1/7', 'Gi2/0/1' ...]
    # и возвращает словарь, если Catalyst 2960S и выше:
    # {'1/0/': [..], 1/1/:[..], 2/0/:[..], ..}
    # иначе Catalyst 2960G:
    # {'0/': [..], 1/: [..], ..}
    dictCatalyst = {}
    for item in outputData:
        item = item.replace('Gi', '').split('/')
        if len(item) == 2: # [0,1] Gi0/1
            if item[0] + '/' not in dictCatalyst:
                dictCatalyst[item[0] + '/']  = []
            dictCatalyst[item[0] + '/'].append(int(item[1]))
        else: # len(item) == 3  [1,0,1] Gi1/0/1
            if item[0] not in dictCatalyst:
                if item[0] + '/' + item[1] +'/' not in dictCatalyst:
                    dictCatalyst[item[0] + '/' + item[1] + '/']  = []
                dictCatalyst[item[0] + '/' + item[1] + '/'].append(int(item[2]))
            elif item[1] != '0':
                if item[0] + '-' + item[1] not in dictCatalyst:
                    dictCatalyst[item[0] + '/' + item[1] + '/'] = []
                dictCatalyst[item[0] + '/' + item[1] + '/'].append(int(item[2]))
    return dictCatalyst
#
def on_off_Ports(command, outputData, nameSwitch = ''):
    reg_exp_sg300 = re.compile(r'iSG|isg')  # Шаблон поиска. Ищем iSG или isg
    handlerSG300['host'] = ' '.join(nameSwitch)
    if re.findall(reg_exp_sg300, ''.join(nameSwitch)):
       try:                 # ---------- SG300 ---------- #
           start = datetime.now().replace(microsecond=0)
           with ConnectHandler(device_type=handlerSG300['device_type'],
                               ip=handlerSG300['host'],
                               username=handlerSG300['user'],
                               password=handlerSG300['password']) as ssh:
               for item in splitArraySG300(outputData):
                   # Отправляем команды в режиме "conf t"
                    ssh.send_config_set([f'{commands[4]}{item[0]}-{item[-1]}', command])
                    print(f'{item} - {command}')
           stop = datetime.now().replace(microsecond=0)
           print(f'Время выполнения: {stop - start}')
       except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print('Error:', error)
    else:
        try:               # ---------- Catalyst ---------- #
            start = datetime.now().replace(microsecond=0)
            with ConnectHandler(device_type=handlerCatalyst['device_type'],
                                ip=handlerCatalyst['host'],
                                username=handlerCatalyst['user'],
                                password=handlerCatalyst['password'],
                                secret=handlerCatalyst['secret']) as ssh:
                for key, value in splitDictCatalyst(outputData).items():
                     for item in splitArrayCatalyst(value):
                         ssh.enable()
                         ssh.send_config_set([f'{commands[5]}{key}{item[0]}-{item[-1]}' ,command])
                         #print(key , value)
                         print(f'{commands[5]}{key}{item[0]}-{item[-1]}' ,command)
            stop = datetime.now().replace(microsecond=0)
            print(f'Время выполнения: {stop - start}')
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            print('Error:', error)
#
def readFile(fileSwitch):
    try:
        with open(fileSwitch) as file:
            for item in file.readlines():
                if item != '\n': # Сотрим пустые строки
                    print(f'{"-" * 34}\nКоммутатор: {item.strip()}\n{"-" * 34}')
                    reg_exp = re.compile(r'iSG|isg') # Шаблон поиска. Ищем SG или sg
                    if re.findall(reg_exp, item):
                        handlerSG300['host'] = item.strip() #
                        sshConnect(item.strip(), handlerSG300)
                    else:
                        handlerCatalyst['host'] = item.strip()#
                        sshConnect(item.strip(), handlerCatalyst)
                else: continue
    except (FileExistsError, FileNotFoundError) as error:
        print('* Error:', error)
#
def run():
    count = 0
    readFile(fileSwitch)
    while True:
        print(f'Включить или выключить порты: "on"/"off"\nВыйти: "Enter"')
        on_off = input('>: ')
        if (on_off == ''): return False
        elif 'on' in on_off:  return on_off_Ports('no sh', dictFSTEK, listNameSwitch)
        elif 'off' in on_off: return on_off_Ports('sh', dictFSTEK, listNameSwitch)
        else:
            count += 1
            if count == 3:
                print('\n'*3)
                print('Xэeee.. внимательнее вводи команду.)', '\n'*3)
                count = 0; continue
            print('* Ошибка. Введена неправильная команда !')
            continue
# run
if __name__ == "__main__":
    run()
