# Импортируем модули
import paramiko
import re
import time

# Параметры подключения
sshParams = {'host': '127.0.0.1',
             'user': 'asumin',
             'password': '*******',
             'port': '22'}

# Команды
commands = ['dfd -ahdf', 'cat /var/log/syslog'] # для примера

# создаем ф-цию sshConnect
def sshConnect(host, user, password, port, command):
    # Ф-ция подкл по протоколу ssh и возвращает словарь с данными.
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=password, port=port, look_for_keys=False, allow_agent=False)
    time.sleep(2)
    # Выполняем
    dictOutput = {'host': '', 'output': []} # добавляем в словрь вывод ф-ции "client.exec_command(command)"
    stdin, stdout, stderr = client.exec_command(command)
    if not stderr.readlines():
        dictOutput['host'] = host
        dictOutput['output'] += stdout.readlines()
    else:
        print(f'Ошибка: Команда {command} не выполнена!')
    #print(dictOutput) # Смотрим listOutput
    # Закрываем соединение
    time.sleep(2)
    client.close()
    return dictOutput
#
def getData():
    for command in commands:
        data = sshConnect(sshParams['host'], sshParams['user'], sshParams['password'], sshParams['port'], command)
        for value in data['output']:
            print(value.split())
#
#--------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # Вызываем ф-цию getData
    getData()

